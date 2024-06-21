from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product
from users.models import User


class ProductTestCaseSeller(APITestCase):

    def setUp(self):  # Исправлена опечатка здесь
        self.user = User.objects.create(email="test@sky.pro", is_seller=True)
        self.user.set_password("test")  # Правильная установка пароля
        self.user.save()
        self.product = Product.objects.create(
            name="Молоко", price=78, seller=self.user, is_sell=True
        )
        self.client.force_authenticate(user=self.user)

    def test_product_retrieve(self):
        url = reverse("products:product_retrieve", args=(self.product.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Молоко")
        expected_price = round(self.product.price / 0.78)
        self.assertEqual(data.get("price"), expected_price)

    def test_product_create(self):
        url = reverse("products:product_create")
        data = {"name": "Кофе", "price": 129, "seller": 1, "is_sell": True}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.all().count(), 2)

    def test_product_update(self):
        url = reverse("products:product_update", args=(self.product.pk,))
        data = {"price": 109}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("price"), 109)

    def test_product_delete(self):
        url = reverse("products:product_delete", args=(self.product.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.all().count(), 0)

    def test_product_list(self):
        url = reverse("products:product")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "name": self.product.name,
                    "description": self.product.description,
                    "price": round(
                        self.product.price / 0.78,
                    ),
                },
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_product_list_seller(self):
        url = reverse("products:list_seller")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.product.id,
                    "name": self.product.name,
                    "description": self.product.description,
                    "price": self.product.price,
                    "seller": 4,
                    "is_sell": self.product.is_sell,
                },
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class ProductTestCaseUser(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@sky.pro")
        self.user.set_password("test")  # Правильная установка пароля
        self.user.save()
        self.product = Product.objects.create(
            name="Молоко", price=78, seller=self.user, is_sell=True
        )
        self.client.force_authenticate(user=self.user)

    def test_product_retrieve(self):
        url = reverse("products:product_retrieve", args=(self.product.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Молоко")
        expected_price = round(self.product.price / 0.78)
        self.assertEqual(data.get("price"), expected_price)

    def test_product_create(self):
        url = reverse("products:product_create")
        data = {"name": "Кофе", "price": 129, "seller": 1, "is_sell": True}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_product_update(self):
        url = reverse("products:product_update", args=(self.product.pk,))
        data = {"price": 109}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_product_delete(self):
        url = reverse("products:product_delete", args=(self.product.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_product_list(self):
        url = reverse("products:product")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "name": self.product.name,
                    "description": self.product.description,
                    "price": round(
                        self.product.price / 0.78,
                    ),
                },
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_product_list_seller(self):
        url = reverse("products:list_seller")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
