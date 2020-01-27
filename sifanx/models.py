from django.db import models
from django.urls import reverse

# Create your models here.


class index_img (models.Model):
    images = models.ImageField(upload_to='images/')

class testmony(models.Model):
    name = models.CharField(max_length = 20)
    comment = models.TextField(max_length = 250)
    images =models.ImageField(upload_to='testimony/',
    default='testimony/def.jpg',
    blank=True,
    null=True)
    def get_absolute_url(self):
        return reverse('Home')
    
class feedback(models.Model):
    feedback = models.TextField(max_length = 200)
    def get_absolute_url(self):
        return reverse('thks')
    
class gallery(models.Model):
    typ = models.CharField(max_length =20)
    img = models.ImageField(upload_to='gallery/')