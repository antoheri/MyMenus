from django.db import models
from django.contrib.auth.models import User

class Receipt(models.Model):
    entree = models.CharField(max_length=200, null=True)
    plat_principal = models.TextField(max_length=200)
    garniture = models.TextField(max_length=200, null=True)
    produit_laitier_ou_divers = models.TextField(max_length=200, null=True)
    dessert = models.TextField(max_length=200, null=True)

    #def __srt__(self):
        #return self.title

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["user", "receipt"]
