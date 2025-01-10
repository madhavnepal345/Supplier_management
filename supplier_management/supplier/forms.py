from django import forms
from .models import Product,Order,Client,Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=['name','description','price','stock','restock_threshold']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields=['product','quantity','customer_name','shipping_address','status']


class ClientForm(forms.ModelForm):
    class Meta:
        model=Client
        fields=['name','contact_details']


class ReviewForm(forms.ModelForm):
    class Meta:
        fields=['rating','comment']


