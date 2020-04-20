from django.contrib import admin

from .models import Category, Product

# Admin class for categories 
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)

# Admin class for products
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'price']#, 'stock', 'available'] # available features
    list_filter = ['category']#['available', 'category'] # features for filtering
    list_editable = ['price']#, 'stock', 'available'] # price field can be edited
    prepopulated_fields = {'slug': ('title',)} # slug is equal title of product

admin.site.register(Product, ProductAdmin) 