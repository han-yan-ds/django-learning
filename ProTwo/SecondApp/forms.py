from django import forms

class FormModel(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField()
    botCatcher = forms.CharField(widget=forms.HiddenInput, required=False) # this catches a bot because a bot will fill out this form, but a user won't (it's hidden)

    def clean_botCatcher(self): # must be named clean_fieldName... look up "Django clean_fields"
        botCatcherText = self.cleaned_data['botCatcher']
        if len(botCatcherText) > 0:
            raise forms.ValidationError("GOTCHA BOT!")
        return botCatcherText
        