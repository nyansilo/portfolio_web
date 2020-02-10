from django.db import models

# Create your models here.
class DogCatModel(models.Model):

	name = models.CharField(max_length = 100)
	#imagefile = models.ImageField(upload_to='dogcats/dataset/', blank=True , null=True)
	imagefile = models.ImageField(upload_to='dogcats/dataset/')

	def __str__(self):
		return self.name