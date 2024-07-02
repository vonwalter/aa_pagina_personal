from django import forms
from .models import Index


class IndexForm(forms.ModelForm):
    class Meta:
        model = Index
        fields = ['nombre', 'foto_de_fondo', 'mi_foto', 'soy_1', 'soy_2', 'soy_3']
