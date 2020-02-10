from django.db import models

# Create your models here.
class CassavaModel(models.Model):

	name = models.CharField(max_length = 100)
	imagefile = models.ImageField(upload_to='cassavas/dataset/')

	def __str__(self):
		return self.name