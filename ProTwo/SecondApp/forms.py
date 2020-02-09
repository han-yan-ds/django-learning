"""
Forms are similar to models in class construction... each class property is now a form-field

We can make good use of arguments in the form-field constructors.  Eg: required=false

We can also make REALLY good use of Django's validators.  
https://docs.djangoproject.com/en/3.0/ref/validators/
"""


from django import forms
# from django.core import validators
from SecondApp.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User # Meta's model property is referencing the model Class (Topic)
        fields = "__all__" # Meta's fields property is referencing a Special Keyword ("__all__")
        