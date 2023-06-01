from django import forms
from .models import Human, Profession
import re
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class HumanForm(forms.ModelForm):
    def clean_Name(self):
        Name = self.cleaned_data['Name']
        if re.search(r'\d', Name):
            raise ValueError('Имя не должно содержать цифр')
        return Name
    def clean_Last_name(self):
        Last_name = self.cleaned_data['Last_name']
        if re.match(r'\d', Last_name):
            raise ValueError('Фамилия не должна содержать цифр')
        return Last_name
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 0:
            raise ValueError('Возраст не может быть отрицательным')
        return age

    captcha = CaptchaField()

    class Meta:
        model = Human
        # fields = '__all__'
        fields = ['Name', 'Last_name', 'biography', 'profession', 'age']
        widgets = {
            'Name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'Last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'age': forms.NumberInput(),
            'biography': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),
            'profession': forms.Select(attrs={
                'class': 'form-control'
            })
        }


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))
    password2 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))
    email = forms.EmailField(label='e-mail', widget=forms.EmailInput(attrs={
        'class': 'form-control'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

