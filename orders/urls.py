from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('gem-ordre/', views.order_create, name='order_create'), # URL for saving order
]