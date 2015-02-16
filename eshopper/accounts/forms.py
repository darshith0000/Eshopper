from django import forms
# from emailusernames.forms import EmailUserCreationForm
#
#
# class UserCreationForm(EmailUserCreationForm):
#
#     def __init__(self, *args, **kwargs):
#         super(UserCreationForm, self).__init__(*args, **kwargs)
#         self.fields["password2"].help_text = ''


class AuthenticationForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'type': 'text'}))
    password = forms.CharField(required=True, max_length = 20, widget=forms.TextInput(attrs={'type':'password' }))