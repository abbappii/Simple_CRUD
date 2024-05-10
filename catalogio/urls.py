from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductList.as_view(), name="product-list-create"),
    path("<int:pk>", views.ProductDetail.as_view(), name="product-detail"),
    path(
        "shipping/tax", views.CalculateShippingTax.as_view(), name="shipping-tax-cost"
    ),
]
