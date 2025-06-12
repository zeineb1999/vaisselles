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
        fields = ['id', 'nom', 'description']

class ProduitSerializer(serializers.ModelSerializer):
    categorie = CategorieSerializer(read_only=True)
    categorie_id = serializers.PrimaryKeyRelatedField(queryset=Categorie.objects.all(), source='categorie', write_only=True)

    class Meta:
        model = Produit
        fields = ['id', 'nom', 'description', 'prix', 'stock', 'image_url', 'categorie', 'categorie_id']

class CommandeProduitSerializer(serializers.ModelSerializer):
    produit = ProduitSerializer(read_only=True)
    produit_id = serializers.PrimaryKeyRelatedField(queryset=Produit.objects.all(), source='produit', write_only=True)

    class Meta:
        model = CommandeProduit
        fields = ['id', 'produit', 'produit_id', 'quantite', 'prix_unitaire']

class CommandeSerializer(serializers.ModelSerializer):
    produits = CommandeProduitSerializer(many=True, read_only=True)

    class Meta:
        model = Commande
        fields = ['id', 'nom', 'prenom', 'numero_telephone', 'adresse', 'livraison_type', 'date_commande', 'statut', 'produits']