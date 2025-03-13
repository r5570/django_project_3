from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=240)
    price=models.PositiveIntegerField()
    rating=models.TextField(max_length=20)
    desc=models.TextField()
    quantity=models.PositiveIntegerField(default=1)

    pic=models.ImageField(upload_to='products/',null=True)
    
    def __str__(self):
        return self.name