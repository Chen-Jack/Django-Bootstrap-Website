from django import forms
from account.models import Entry

class NewEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['user', 'title', 'text']
