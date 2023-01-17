from django import forms
from django.contrib.auth.models import User
from django.test import TestCase



TEST_DATA = {
    "email": "jamesjack@gmail.com",
    "password": "djangonetflix2023",
    "password_conf": "djangonetflix2023"
}





class RegisterForm(forms.Form):
    """Registration form class."""

    firstname = forms.CharField(label="First name")
    lastname = forms.CharField(label="Last name")
    email = forms.EmailField(label="Email Address")
    password = forms.CharField(label="Password", widget=forms.PasswordInput(render_value=True),min_length=8,max_length=22)
    '''render_value=true keeps val of pw even when form is returned with errors'''
    password_conf = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(render_value=True),min_length=8,max_length=22)


    '''adding methods to validate pw'''
    def clean(self):
        super(RegisterForm,self).clean()
        '''getting email to check if it already exists in database'''
        email=self.cleaned_data['email']
        password=self.cleaned_data['password']
        password_conf=self.cleaned_data['password_conf']

        if password!=password_conf:
            self.errors['password_conf']=self.error_class(["password doesnt match"])
        if User.objects.filter(username=email).exists():
            self.errors['email']=self.error_class(["email already exists"])

        return self.cleaned_data

class LoginForm(forms.Form):
    """Login form class."""

    email = forms.EmailField(label="Email Address")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class SearchForm(forms.Form):
    '''creating search bar form'''
    search_val=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Search'}))
    


class RegisterTests(TestCase):

    def test_get_registration_page(self):
        pass

    def test_registration_with_valid_data(self):
        pass

    def test_registration_with_empty_fields(self):
        pass

    def test_registration_with_wrong_password_confirmation(self):
        pass