from django import forms

from django import forms
from .models import AddToListModel

class AddToListForm(forms.ModelForm):
    class Meta:
        model = AddToListModel
        fields = '__all__'

