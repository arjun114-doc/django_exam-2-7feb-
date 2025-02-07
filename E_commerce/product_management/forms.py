from django import forms
from product_management.models import Review,Product


class Productform(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"
    
class Reviewform(forms.ModelForm):
    class Meta:
        model=Review
        # fields=['reviewer_name','rating','comment']
        fields="__all__"
    
    

    
        
    
