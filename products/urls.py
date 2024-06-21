from django.urls import path

from products.apps import ProductsConfig
from products.views import (ProductCreateApiView, ProductDestroyApiView,
                            ProductListApiView, ProductListApiViewSeller,
                            ProductRetrieveApiView, ProductUpdateApiView)

app_name = ProductsConfig.name
urlpatterns = [
    path("", ProductListApiView.as_view(), name="product"),
    path("seller/", ProductListApiViewSeller.as_view(), name="list_seller"),
    path("<int:pk>/", ProductRetrieveApiView.as_view(), name="product_retrieve"),
    path("create/", ProductCreateApiView.as_view(), name="product_create"),
    path("update/<int:pk>/", ProductUpdateApiView.as_view(), name="product_update"),
    path("delete/<int:pk>/", ProductDestroyApiView.as_view(), name="product_delete"),
]
