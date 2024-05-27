from django.db import models

# Create your models here.
#coloane: name, description, ingredients,price, weight_grams,
# available_quantity, image
class Product(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	ingredients = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2) # adica sa imi afiseze cu exact 2 zecimale
	weight_grams = models.IntegerField()
	available_quantity = models.IntegerField(default=1)
	image = models.ImageField(upload_to="product_images", null=True, blank=True) # locatia (folder) unde se vor salva imaginile uploadate din interfata

	def __str__(self):
		return self.name



"""
image = models.ImageField(upload_to="product_images", null=True, blank=True) 
# locatia (folder) unde se vor salva imaginile uploadate din interfata
# Poate sa nu fie nici una none=True
#Poate sa fie si fara poza adica blank=True
"""

