from django import forms
from .models import Quincena

class DuplicarGastosForm(forms.Form):
    origen = forms.ModelChoiceField(
        queryset=Quincena.objects.all(),
        label="Quincena de origen",
        help_text="Selecciona la quincena de la que deseas copiar los gastos"
    )
    destino = forms.ModelChoiceField(
        queryset=Quincena.objects.all(),
        label="Quincena de destino",
        help_text="Selecciona la quincena a la que se copiarán los gastos"
    )

    def clean(self):
        cleaned_data = super().clean()
        origen = cleaned_data.get("origen")
        destino = cleaned_data.get("destino")
        if origen == destino:
            raise forms.ValidationError("La quincena de origen y destino no pueden ser la misma.")
