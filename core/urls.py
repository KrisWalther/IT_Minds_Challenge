from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.product_list_view, name='product_list'), # URL for product list
    path('<slug:category_slug>/', views.product_list_view, name='product_list_by_category'), # URL for category 
    path('<int:id>/<slug:slug>/', views.product_detail_view, name='product_detail'), # URL for product
]