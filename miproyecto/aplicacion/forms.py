from django import forms

class LibroForm(forms.Form):
    titulo = forms.CharField(max_length=80, required=True)
    autor = forms.CharField(max_length=60, required=True)
    precio = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    genero = forms.CharField(max_length=40, required=True)
    celContacto = forms.IntegerField(required=True)
    emailContacto = forms.EmailField(required=True)

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=40, required=True)
    apellido = forms.CharField(max_length=40, required=True)
    email = forms.EmailField(required=True)
    contraseña = forms.CharField(max_length=10, required=True)

class ComentarioForm(forms.Form):
    texto = forms.CharField(max_length=100, required=True)
    usuario = forms.CharField(max_length=80, required=True)