from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Receipt, Favourite

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password" : {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ["id", "entree", "plat_principal", "garniture", "produit_laitier_ou_divers", "dessert"]
        extra_kwargs = {"author": {"read_only": True}}

class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = ["id", "user", "receipt"]
        extra_kwargs = {"user": {"read_only": True}}