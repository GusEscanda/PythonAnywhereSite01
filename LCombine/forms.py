from django import forms

class MainForm(forms.Form):
    letters     = forms.CharField(label='Letters', help_text='The list of characters to combine')
    length      = forms.IntegerField(label='Length', help_text='Number of letters to combine', initial=0)
    filterFrom  = forms.CharField(label='From', help_text='Display only words alphabetically greater than or equal to...', initial='', required=False)
    filterUntil = forms.CharField(label='Until', help_text='Display only words alphabetically less than or equal to...', initial='', required=False)
    useDict     = forms.BooleanField(label='Use Dict', initial=True, required=False, help_text='Check to display only words in the installed dictionary')

