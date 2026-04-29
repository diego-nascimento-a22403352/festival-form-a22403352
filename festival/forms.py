from django import forms
from .models import Concerto, Palco

class ConcertoForm(forms.ModelForm):
    class Meta:
        model = Concerto
        # Ponto 2 - Alterado para __all__ para permitir editar todos os campos
        fields = "__all__"


class PalcoForm(forms.ModelForm):
    class Meta:
        model = Palco
        # Ponto 7 - Alterado para __all__ para permitir editar os campos do palco
        fields = "__all__"