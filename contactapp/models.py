from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.

class Contacts(models.Model):

    ## contain all the products informations
    heading = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    workhr = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10,decimal_places=5)
    image = models.ImageField(upload_to='contacts/' , blank=True , null=True)
    url = models.URLField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True  , null=True)
    
    def save(self , *args , **kwargs):
        if not self.slug and self.heading :
            self.slug = slugify(self.heading)
        super(Contacts , self).save(*args , **kwargs)
    


    def __str__(self):
        return self.heading





