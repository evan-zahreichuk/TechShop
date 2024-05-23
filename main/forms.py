# forms.py
from django import forms
from .models import Product

class BrandFilterForm(forms.Form):
    brand_choices = [(brand, brand) for brand in Product.objects.order_by('brand').values_list('brand', flat=True).distinct()]
    brand = forms.ChoiceField(
        choices=[('', 'All makrs')] + brand_choices,
        required=False,
        label="Choose mark"
    )



