from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    email = forms.CharField(max_length=65)


class SSHConnectionForm(forms.Form):
    username = forms.CharField(max_length=255)
    host = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    port = forms.IntegerField()

