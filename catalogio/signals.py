
# Update product price depending on user input
def update_price(sender, instance, **kwargs):
    decimal_value = instance.price - int(instance.price)

    # Check if the decimal part is less than or equal to 0.5
    if decimal_value <= 0.5:
        instance.price = int(instance.price) + 0.55
    else:
        instance.price = int(instance.price) + 0.99