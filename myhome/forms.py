from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Mensagem,Cadastro
from django import forms


class FormHome(forms.Form):
    email=forms.EmailField(label=False)

class CriarContaForm(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model= Usuario
        fields=( 'username', 'email','password1', 'password2')

class CadastroForm(forms.ModelForm):

    class Meta:
        model= Cadastro
        exclude=('meu_usuario','data')

class ContatoForm(forms.ModelForm):

    class Meta:
        model= Mensagem
        exclude=['visualizado','data']
