from django.db import models

class Product(models.Model):
   
    name = models.CharField(max_length = 200) 
    price= models.PositiveIntegerField()
    desc =models.TextField()
    stock=models.PositiveIntegerField(default=1)


    pic = models.ImageField(upload_to='products/',null = True)

    def __str__(self):
        return self.name