from django import forms

class FormularioContacto(forms.Form):
    

    nombre=forms.CharField(empty_value='Nombre', required=True, max_length=50,)
    email=forms.EmailField(label='Email', required=True, max_length=50,)
    contenido=forms.CharField(label='Contenido',required=False, max_length=10000, widget=forms.Textarea)