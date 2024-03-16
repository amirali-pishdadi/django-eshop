from rest_framework import serializers
from .models import *


class GetProductById(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
