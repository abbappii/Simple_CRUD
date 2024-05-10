from rest_framework import serializers
from .models import Product


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
            "updated_at",
        )
        read_only_fields = ("pk", "created_at", "updated_at")

    """
    unique name check
    """

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

    def create(self, validated_data):
        from catalogio.tasks import send_mail_to_seller

        validated_data["user"] = self.context["request"].user
        product = super().create(validated_data)

        title = product.title
        email = product.user.email

        # sending email to seller(creator of the product)
        send_mail_to_seller.delay(title, email)

        return product
