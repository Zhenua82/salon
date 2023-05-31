from django import forms
from .models import Human, Profession
import re
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

# class HumanForm(forms.Form):
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


    # title = forms.CharField(max_length=150, label='Заголовок', widget=forms.TextInput(attrs={
    #     'class': 'form-control'
    # }))
    # content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={
    #     'class': 'form-control',
    #     'rows': 5
    # }))
    # is_published = forms.BooleanField(label='Публикация', initial=True)
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Выберите категорию', widget=forms.Select(attrs={
    #     'class': 'form-control'
    # }))
    # profession = forms.ModelChoiceField(queryset=Profession.objects.all(), label='Категория',
    #                                     empty_label='Выберите категорию')