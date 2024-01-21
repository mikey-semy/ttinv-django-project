from django import forms
from .models import Requests

class Requests(forms.ModelForm):
    class Meta:
        model = Requests
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
            'inn': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'message': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }