from django.db import models
from django.conf import settings
from django.urls import reverse

# Category class
class Category(models.Model):

    # Features
    title = models.CharField(max_length=64, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    # Meta data
    class Meta:
        ordering = ('title',) # sort categories by title
        verbose_name = 'category' # singular name
        verbose_name_plural = 'categories' # plural name

    def __str__(self):
        return self.title
    
    # Canonical URL
    def get_absolute_url(self):
        return reverse('core:product_list_by_category', args=[self.slug])

# Product class
class Product(models.Model):
    # Features
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=64, db_index=True)
    slug = models.SlugField(max_length=64, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.PositiveSmallIntegerField()

    # Meta data
    class Meta:
        ordering = ('title',) # sort products by title
        index_together = (('id', 'slug'),) # unique indexing

    def __str__(self):
        return self.title

    # Canonical URL
    def get_absolute_url(self):
        return reverse('core:product_detail', args=[self.id, self.slug])
