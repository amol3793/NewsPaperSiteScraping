"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import TextInput


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))



class BootstrapUserCreationForm(UserCreationForm):

    username = forms.RegexField(label=_("User Name"), max_length=30, regex=r"^[\w.@+-]+$",
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                    "@/./+/-/_ only.\n"),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")},
        widget=TextInput(attrs={'class': 'form-control',
                                'required': 'true',
                                'placeholder': 'User name'
                            
        }))

    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'required': 'true',
                                          'placeholder': 'Enter Password'

        }))
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'type': 'password',
                                          'required': 'true',
                                          'placeholder': 'Enter Password Again'
        }),
        help_text=_("Enter the same password as above, for verification."))

    first_name = forms.CharField(label=_("\nName"),
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'text',
                                      'required': 'true',
                                      'placeholder': 'Name'
        }),
        help_text=_("Enter user first and last name."))

    email = forms.CharField(label=_("\nEmail"),
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'email',
                                      'placeholder': 'Email address',
                                      'required': 'true',
                                      'placeholder': 'Email'
        }))
