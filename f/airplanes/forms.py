from django import forms
from .models import *
from django.contrib.auth.models import User

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['code', 'city']
        help_texts = { "code": "Introduce un codigo unico para el aeropuerto" }

    def clean_code(self):
        code = self.cleaned_data["code"]

        if Airport.objects.filter(code__iexact=code).exists():
            raise forms.ValidationError("Este codigo ya existe")
        if len(code) != 3:
            raise forms.ValidationError("El codigo debe ser de 3 caracteres")


        return code

    def clean_city(self):
        city = self.cleaned_data["city"]

        if city.lower() == "masaya":
            raise forms.ValidationError("Masaya no tiene aeropuerto")

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label="Introduce tu contraseña", widget=forms.PasswordInput)
    confirmation = forms.CharField(label="Confirma tu contraseña", widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_confirmation(self):
        cd = self.cleaned_data
        # 'DROP DATABASE'
        
        if cd['password'] != cd['confirmation']:
            raise forms.ValidationError(" Las contraseñas no coinciden ") 

