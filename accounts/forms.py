# forms.py

from django import forms
from .models import Contact
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'inputAge': forms.DateInput(attrs={'type': 'date'}),
            'inputPhoneNumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Başında sıfır olmadan 10 hane olarak'}),
            'inputUsername': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Mail adresiniz'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Bize iletmek istedikleriniz'}),
            'inputPassword1': forms.PasswordInput(),  # Use PasswordInput widget for password
            'inputPassword2': forms.PasswordInput(),

        }     

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('inputPassword1')
        password2 = cleaned_data.get('inputPassword2')

        if password1 != password2:
            self.add_error('inputPassword2', 'Şifreler eşleşmiyor.')

        return cleaned_data
    

