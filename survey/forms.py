from django import forms
from .models import Survey

class ItemForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = [
            'item1',
            'item2',
            'item3',
            'item4',
            'item5',
            'item6',
            'item7',
            'item8',
            'item9',
            'item10',
        ]
