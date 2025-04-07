from rest_framework import serializers
from .models import product, category, review


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = '__all__'

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = '__all__'