from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'), # URL for cart view
    path('tilføj/<int:product_id>/', views.cart_add, name='cart_add'), # URL for adding product
    path('fjern/<int:product_id>/', views.cart_remove, name='cart_remove'), # URL for removing product
]