from django import forms
from account.models import Entry

class EntryForm(forms.ModelForm):
    title = forms.CharField(max_length = 50)
    class Meta:
        model = Entry
        fields = ['title', 'text']
