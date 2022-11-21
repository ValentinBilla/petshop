from django import forms
from .models import Animal

class MoveForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = ('spot',)
        widgets = {
            'spot': forms.Select(attrs={'class': 'inline mx-2 rounded-full bg-slate-500'}),
        }