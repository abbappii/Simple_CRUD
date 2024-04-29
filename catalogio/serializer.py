
from rest_framework import serializers
from .models import Product
from rest_framework import status
from rest_framework.generics import ValidationError

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            "pk",
            "title",
            "price",
            "manufacturer_company_name",
            "discount",
            "stock",
            "is_available_after_stock",
            "created_at",
            "updated_at"
        )
        read_only_fields = ("pk", "created_at", "updated_at")


    '''
    unique name check
    '''
    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title cannot be empty")
        if self.instance:
            queryset = Product.objects.exclude(pk=self.instance.pk)
        else:
            queryset = Product.objects.all()

        if queryset.filter(title=value).exists():
            raise serializers.ValidationError("Product already exists with this name")
        return value