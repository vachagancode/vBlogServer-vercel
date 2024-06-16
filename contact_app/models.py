from django.db import models

# Create your models here.
class ContactFormData(models.Model):
	name = models.CharField(max_length=52)
	email = models.EmailField(max_length=254)
	message = models.TextField()

	date_sent = models.DateTimeField(auto_now_add=True)
