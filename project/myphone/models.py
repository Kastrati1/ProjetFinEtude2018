from django.db import models

class Produit(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
