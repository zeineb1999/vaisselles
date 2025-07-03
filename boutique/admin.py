from django.contrib import admin

from .models import Utilisateur

admin.site.register(Utilisateur)
from .models import Categorie, Produit, Commande, CommandeProduit
admin.site.register(Categorie)
admin.site.register(Produit)    
admin.site.register(Commande)
admin.site.register(CommandeProduit)
from django.contrib.auth.admin import UserAdmin

