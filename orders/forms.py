from django import forms
from .models import Order

# Class for order form (email only)
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['email']