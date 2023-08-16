from django import forms

from .models import Product

from main.main import main

class ProductForm(forms.ModelForm):
    sujet       = forms.CharField(required=False, 
                        widget=forms.Textarea(attrs={
                                    "placeholder": "Les cosmétiques au café",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 8,
                                    'cols': 61}))
    image   = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "graines de cafés, cosmétiques au café",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 5,
                                    'cols': 60
                                }
                            )
                        )
    
    class Meta:
        model = Product
        fields = [
            'sujet',
            'image'
        ]


class RawProductForm(forms.Form):
    prompt       = forms.CharField(required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    imgKeyWord   = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )