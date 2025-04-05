from django.urls import path
from . import views



urlpatterns =[
    
    path('',views.home,name='homepage'),
    path('mail',views.mail,name='mail_page'),
    path('product/',views.productlist,name='productpage'),
    path('product/<int:id>',views.product_details,name='prod_details'),
    path('product/add',views.AddProduct.as_view(),name='add_prod'),
    path('product/edit/<int:pk>',views.EditProduct.as_view(),name='edit_prod'),
    path('product/del/<int:pk>',views.DelProduct.as_view(),name='del_prod'),
     path('products/search', views.searchView, name = 'prod_search')
      
]