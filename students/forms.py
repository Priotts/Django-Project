from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#defining the form for the user to sign up
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
    
    #validating first_name and last_name
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.isalpha():
            raise forms.ValidationError("The name must contain only alphabetical characters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name.isalpha():
            raise forms.ValidationError("The surname must contain only alphabetical characters.")
        return last_name  