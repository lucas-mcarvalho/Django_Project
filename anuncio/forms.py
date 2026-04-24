from anuncio.models import Anuncio
from django import forms
class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        exclude = []