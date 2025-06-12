from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include
router = DefaultRouter()

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    path('api/logout/', LogoutView.as_view(), name='logout'),  # Ajout de la route pour la déconnexion
    
    # Categorie
    path('categories/', CategorieListCreateView.as_view()),
    path('categories/<int:pk>/', CategorieRetrieveUpdateDestroyView.as_view()),

    # Produit
    path('produits/', ProduitListCreateView.as_view()),
    path('produits/<int:pk>/', ProduitRetrieveUpdateDestroyView.as_view()),

    # Commande
    path('commandes/', CommandeListCreateView.as_view()),
    path('commandes/<int:pk>/', CommandeRetrieveUpdateDestroyView.as_view()),

    # CommandeProduit
    path('commande-produits/', CommandeProduitListCreateView.as_view()),
    path('commande-produits/<int:pk>/', CommandeProduitRetrieveUpdateDestroyView.as_view()),
] + router.urls