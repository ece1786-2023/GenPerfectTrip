from django import forms

class UserInputForm(forms.Form):
    user_input = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'custom-input white-text',
            'id': 'user_input',
            'autofocus': 'autofocus',
            'placeholder': 'I want to go to New York for three days.'
        })
    )