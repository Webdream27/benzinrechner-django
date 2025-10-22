from django import forms

class BenzinForm(forms.Form):
    kilometer = forms.FloatField(label="Gefahrene Kilometer")
    verbrauch = forms.FloatField(label="Verbrauch (Liter pro 100 km)")
    preis = forms.FloatField(label="Preis pro Liter (€)")



