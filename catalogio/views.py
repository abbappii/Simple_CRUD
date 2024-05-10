
from rest_framework import generics

from .models import Product
from .serializer import ProductSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model

User = get_user_model()
"""
    Product CRUD
"""

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    permission_classes = []

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    permission_classes = []
    lookup_field = "pk"


"""
to shown user shipping cost and tax when try to buy product.
we will call this api when a user will checkout and ready to order a product
"""

# simple mapping for tax and shipping_cost to evaluate this api
tax = {"Dhaka": 0.12, "Rajshahi": 0.30, "Chittagong": 1.0, "Sylhet": 2.4}
shipping_cost = {"Dhaka": 70, "Others": 130}


class CalculateShippingTax(APIView):
    permission_classes = []

    def post(self, request, **kwargs):
        user_id = request.data.get("user_id")
        product_price = request.data.get("product_price")
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found with this pk."},
                status=status.HTTP_204_NO_CONTENT,
            )

        try:
            # address of user
            city = user.city
            state = user.state
            country = user.country

            shipping_cost = calculate_shipping_cost(city)
            tax_rate = calculating_tax_rate(city)
            total_amount = product_price + shipping_cost + (product_price * tax_rate)
            return Response(
                {
                    "shipping_cost": shipping_cost,
                    "tax_rate": tax_rate,
                    "checkout_product_price": product_price,
                    "total_amount": total_amount,
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


def calculate_shipping_cost(city):
    return shipping_cost.get(city, 120)


def calculating_tax_rate(city):
    return tax.get(city, 0.0)

