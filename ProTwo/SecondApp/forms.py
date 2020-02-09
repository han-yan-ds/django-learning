"""
Forms are similar to models in class construction... each class property is now a form-field

We can make good use of arguments in the form-field constructors.  Eg: required=false

We can also make REALLY good use of Django's validators.  
https://docs.djangoproject.com/en/3.0/ref/validators/
"""


from django import forms
# from django.core import validators
from SecondApp.models import User

class FormModel(forms.ModelForm):
    class Meta:
        model = User # Meta's model property is referencing the model Class (Topic)
        fields = "__all__" # Meta's fields property is referencing a Special Keyword ("__all__")


# def exampleCustomValidator(value):
#     # Demo's the structure of a custom validator
#     if value[-10:] != "@gmail.com":
#         raise forms.ValidationError("Must be a Gmail email address")

# class FormModel(forms.Form):
#     name = forms.CharField(label="Full Name") # label is the HTML-displayed name of the field... default is capitalized fieldname
#     email = forms.EmailField(validators=[exampleCustomValidator])
#     verifyEmail = forms.EmailField()
#     text = forms.CharField()
#     botCatcher = forms.CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)]) # this catches a bot because a bot will fill out this form, but a user won't (it's hidden)

#     def clean(self):
#         allCleanData = super().clean() # this is a dictionary that has all fields with their values
#         email = allCleanData['email']
#         verifyEmail = allCleanData['verifyEmail']
#         if (email != verifyEmail):
#             raise forms.ValidationError("Email addresses must match!")
        