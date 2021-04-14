from django import forms

class MainForm(forms.Form):
    
    LANGUAGES = [
        ('en', 'English'),
        ('es', 'Spanish'),
        ('af', 'Afrikaans'),
        ('bg', 'Bulgarian'),
        ('br', 'Breton'),
        ('ca', 'Catalan'),
        ('cs', 'Czech'),
        ('da', 'Danish'),
        ('de', 'German'),
        ('eo', 'Esperanto'),
        ('et', 'Estonian'),
        ('fr', 'French'),
        ('ga', 'Irish'),
        ('gl', 'Galician'),
        ('hr', 'Croatian'),
        ('hu', 'Hungarian'),
        ('id', 'Indonesian'),
        ('is', 'Icelandic'),
        ('it', 'Italian'),
        ('lt', 'Lithuanian'),
        ('nl', 'Dutch'),
        ('no', 'Norwegian'),
        ('pl', 'Polish'),
        ('ro', 'Romanian'),
        ('ru', 'Russian'),
        ('sk', 'Slovak'),
        ('sl', 'Slovenian'),
        ('sv', 'Swedish'),
        ('uk', 'Ukrainian'),
        ('uz', 'Uzbek'),
        ('zu', 'Zulu'),
    ]
    
    letters     = forms.CharField(label='Letters', help_text='The list of characters to combine')
    length      = forms.IntegerField(label='Length', help_text='Number of letters to combine', initial=0)
    filterFrom  = forms.CharField(label='From', help_text='Display only words alphabetically greater than or equal to...', initial='', required=False)
    filterUntil = forms.CharField(label='Until', help_text='Display only words alphabetically less than or equal to...', initial='', required=False)
    useDict     = forms.BooleanField(label='Use Dict', initial=True, required=False, help_text='Check to display only words in the installed dictionary')
    langTag     = forms.ChoiceField(label='Language', help_text='The language of the dictionary', initial='en', required=False, choices=LANGUAGES)

