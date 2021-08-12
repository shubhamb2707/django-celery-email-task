from django import forms
from django.contrib.auth.models import User
  
# creating a form
class UserForm(forms.Form):
    '''This form accepts one field : number_of_users'''
    number_of_users = forms.IntegerField(
        label = 'Enter the number of users you want to create',
        widget = forms.NumberInput(
            attrs = {'class': 'form-control', 'placeholder': 'Enter an integer value'}
        )
    )

class EmailForm(forms.Form):
    '''This form accepts one field : subject, message'''
    mail_subject = forms.CharField(
        label = 'Enter Subject',
        widget = forms.TextInput(
            attrs = {'class': 'form-control', 'placeholder': 'Enter subject'}
        )
    )
    message = forms.CharField(
        label = 'Enter message',
        widget = forms.Textarea(
            attrs = {'class': 'form-control', 'placeholder': 'Enter message'}
        )
    )