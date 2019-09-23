from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    icon1 = models.ImageField(upload_to='images/')
    icon2 = models.ImageField(upload_to='images/')
    icon3 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Bike(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    icon1 = models.ImageField(upload_to='images/')
    icon2 = models.ImageField(upload_to='images/')
    icon3 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title