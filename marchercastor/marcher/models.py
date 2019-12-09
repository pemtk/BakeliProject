from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    # pk aka id --> numbers
    nom_cat     = models.CharField(max_length=120, null=True, blank=True)
    images      = models.ImageField(upload_to='media/', null=True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_cat


class Products(models.Model):
    # pk aka id --> numbers
    name        = models.CharField(max_length=120, null=True, blank=True)
    price       = models.CharField(max_length=120, null=True, blank=True)
    images       = models.ImageField(upload_to='media/', null=True, blank=True)
    categories  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.categorie.username)