from django import forms
from .models import *
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
