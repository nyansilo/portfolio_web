from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.


"""
class ProjectApi(models.Model):

    ## contain all the products informations
    name = models.CharField(max_length=200)
    technology = models.CharField(max_length=200)
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10,decimal_places=5)
    category = models.ForeignKey('Category' , on_delete=models.SET_NULL , null=True)
    image = models.ImageField(upload_to='main_project/' , blank=True , null=True)
    url = models.URLField(max_length=200, blank=True , null=True)
    created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True  , null=True)
   
    def __str__(self):
        return self.name

"""

class Project(models.Model):

    ## contain all the products informations
    name = models.CharField(max_length=200)
    technology = models.CharField(max_length=200)
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10,decimal_places=5)
    category = models.ForeignKey('Category' , on_delete=models.SET_NULL , null=True)
    image = models.ImageField(upload_to='main_project/' , blank=True , null=True)
    url = models.URLField(max_length=200, blank=True , null=True)
    created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True  , null=True)
    
    def save(self , *args , **kwargs):
        if not self.slug and self.name :
            self.slug = slugify(self.name)
        super(Project , self).save(*args , **kwargs)
    


    def __str__(self):
        return self.name



class ProjectImages(models.Model):
    project = models.ForeignKey(Project , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/' , blank=True , null=True)

    def __str__(self):
        return self.project.name

    class Meta:
        verbose_name = 'Project Image'
        verbose_name_plural = 'Project Images'


class Category(models.Model):
    ## for product category
    category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/' , blank=True , null=True)
    """
    slug = models.SlugField(blank=True  , null=True)


    def save(self , *args , **kwargs):
        if not self.slug and self.category_name :
            self.slug = slugify(self.category_name)
        super(Category , self).save(*args , **kwargs)
    """
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name
