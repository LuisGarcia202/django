from django import forms
from .models import Libro,Compra
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['nombre','autor','codigo']
        labels = {
            'nombre': 'Nombre',
            'autor': 'autor',
            'codigo': 'Codigo'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'})
        }

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['libro', 'fecha', 'cantidad']
        widgets = {
            'libro': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['libro'].queryset = Libro.objects.all()


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}), validators=[])
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}