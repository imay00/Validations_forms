from django import forms 
from .models import Product


class PrdForum(forms.ModelForm):
    tax_price=forms.FloatField()
    class Meta:
        model=Product
        fields='__all__'
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": f" form-control {field}"})
    
    
    def clean(self):
        price=self.cleaned_data.get("price")
        discount=self.cleaned_data.get("discount_price",0)
        tax=self.cleaned_data.get("tax_price",0)
        
        if (price+tax-discount)==0:
            raise forms.ValidationError("Price tax_price ve discount_prc'in ferqinden boyuk olmalidir.")
        return super().clean()
            