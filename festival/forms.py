from django import forms
from .models import Concerto, Palco

class ConcertoForm(forms.ModelForm):
    class Meta:
        model = Concerto
        fields = "__all__"


class PalcoForm(forms.ModelForm):
    class Meta:
        model = Palco
        fields = "__all__"