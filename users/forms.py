
from .models import User
from django import forms

class registerUserForms(forms.ModelForm):
    password=forms.CharField(label='Senha',widget=forms.PasswordInput(attrs={'placeholder':'Digite sua senha'}))

    password_confim=forms.CharField(label='Confirmar Senha',widget=forms.PasswordInput(attrs={'placeholder':'Confirme sua senha'}))

    username=forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'placeholder':'Digite seu usuario'}))
    class Meta:
        model =  User
        fields = ['user_type','name','username','state',
                'email','phone','profile_photo',
                'cep','street','number',
                'complement','neighborhood','city']

class loginForm(forms.Form):

    username=forms.CharField(label='Usuário',widget=forms.TextInput(attrs={'placeholder':"Digite seu usuario"}))
    password=forms.CharField(label='Senha',widget=forms.TextInput(attrs={'placeholder':"Digite sua senha"}))