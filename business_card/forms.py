from django import forms
from .models import Request

class Request(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
            'inn': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'message': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }