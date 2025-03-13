from django.db import models

from mainapp.models import Product 

from django.contrib.auth.models import User 

class CartItem(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

   
    quantity = models.PositiveIntegerField(default=0)
    
  
    date_added  = models.DateField(auto_now_add=True)

    
    
    # string representation of CartItem object
    def __str__(self):
        return f"Product: {self.product.name} - Count: {self.quantity}"
    
    # method to find total price of particular item in cart
    def get_total_price(self):
        return self.quantity * self.product.price