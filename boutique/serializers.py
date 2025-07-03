from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}
     
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class ProduitSerializer(serializers.ModelSerializer):
    categorie= serializers.PrimaryKeyRelatedField(queryset=Categorie.objects.all())  # Accepte un ID

    
    class Meta:
        model = Produit
        fields = '__all__'

class CommandeProduitSerializer(serializers.ModelSerializer):
    produit = ProduitSerializer(read_only=True)
    produit_id = serializers.PrimaryKeyRelatedField(queryset=Produit.objects.all(), source='produit', write_only=True)

    class Meta:
        model = CommandeProduit
        fields = '__all__'

class CommandeSerializer(serializers.ModelSerializer):
    produits = CommandeProduitSerializer(many=True, read_only=True)

    class Meta:
        model = Commande
        fields = '__all__'