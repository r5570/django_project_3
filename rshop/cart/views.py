from django.shortcuts import render, redirect
from mainapp.models import Product
from .models import CartItem
from django.contrib.auth.decorators import login_required


# implementing AJAX to update cart item quantity without refresh
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


# Create your views here.

# C - Creating cart items
@login_required
def addToCart(request, product_id):
    this_product = Product.objects.get(id = product_id)
    cart_item, created = CartItem.objects.get_or_create(product = this_product, user = request.user)
    cart_item.quantity += 1
    cart_item.save() 

    return redirect('view_cart')

# R - Read Cartitems
@login_required
def viewCart(request):
    template = 'cart.html'
    cart_items = CartItem.objects.filter(user = request.user) 
    total_price = sum(float(item.product.price) * item.quantity for item in cart_items)

    context = {
        'cart_items' : cart_items,
        'total_price' : total_price
    }
    return render( request, template, context)

@login_required
def removeFromCart(request, cart_item_id):
    this_cart_item = CartItem.objects.get(id = cart_item_id)
    this_cart_item.delete()
    return redirect('view_cart')

@login_required
def add_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    overall_total = sum(item.get_total_price() for item in CartItem.objects.filter(user=request.user))
    return JsonResponse({'quantity': cart_item.quantity, 'total_price': cart_item.get_total_price(), 'overall_total': overall_total})

@login_required
def remove_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        overall_total = sum(item.get_total_price() for item in CartItem.objects.filter(user=request.user))
        return JsonResponse({'quantity': cart_item.quantity, 'total_price': cart_item.get_total_price(), 'overall_total': overall_total})
    else:
        cart_item.delete()
        overall_total = sum(item.get_total_price() for item in CartItem.objects.filter(user=request.user))
        return JsonResponse({'quantity': 0, 'total_price': 0, 'overall_total': overall_total})