from rest_framework import serializers
from bloodhound.core.models import Product

# Serializers define the API representation.
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
