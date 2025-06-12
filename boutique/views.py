from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Vue de connexion
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
from django.db.models import ProtectedError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Récupérer le jeton d'actualisation depuis la requête
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response({"error": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

            # Révoquer le jeton d'actualisation
            token = RefreshToken(refresh_token)
            token.blacklist()  # Ajoute le jeton à la liste noire
            return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "An error occurred during logout."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

# Create your views here.
# --- Categorie ---
class CategorieListCreateView(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class CategorieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer


# --- Produit ---
class ProduitListCreateView(generics.ListCreateAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class ProduitRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer


# --- Commande ---
class CommandeListCreateView(generics.ListCreateAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

class CommandeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer


# --- CommandeProduit ---
class CommandeProduitListCreateView(generics.ListCreateAPIView):
    queryset = CommandeProduit.objects.all()
    serializer_class = CommandeProduitSerializer

class CommandeProduitRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommandeProduit.objects.all()
    serializer_class = CommandeProduitSerializer