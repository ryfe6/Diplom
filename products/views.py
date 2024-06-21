from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.paginations import CustomPagination
from products.serializer import ProductSerializer, ProductSerializerSeller
from users.permissions import IsSeller, IsSellerObject


class ProductCreateApiView(CreateAPIView):
    """Создание продукта на маркетплейсе."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializerSeller
    permission_classes = [IsAuthenticated, IsSeller]

    def perform_create(self, serializer):
        product = serializer.save()
        product.seller = self.request.user
        product.save()


class ProductListApiView(ListAPIView):
    """Просмотр продуктов выставленных на продажу."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination


class ProductListApiViewSeller(ListAPIView):
    """Продавец может просматривать свои продукты."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializerSeller
    permission_classes = [IsAuthenticated, IsSeller]
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(seller=user)


class ProductRetrieveApiView(RetrieveAPIView):
    """Пользователь может посмотреть подробную информацию о продукте."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductUpdateApiView(UpdateAPIView):
    """Продавец может менять информацию о своем продукте."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializerSeller
    permission_classes = [IsAuthenticated, IsSeller, IsSellerObject]


class ProductDestroyApiView(DestroyAPIView):
    """Продавец может удалять свой продукт с маркетплейса."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializerSeller
    permission_classes = [IsAuthenticated, IsSeller, IsSellerObject]
