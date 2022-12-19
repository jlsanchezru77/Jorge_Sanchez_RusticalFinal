from django import forms
from django.forms import ModelForm
from .models import Interes1


class UsuarioFormulario(forms.Form):
    Nombre=forms.CharField(max_length=40)
    Apellidos=forms.CharField(max_length=40)
    Edad=forms.IntegerField()

class CompraFormulario(forms.Form):
    Peso=forms.IntegerField()
    Unidades=forms.IntegerField()    


#STATUS =(
 #   ("Compra", "Me interesa adquirir Orellanas"),
  #  ("Cultivo", "Me interesa cultivar Orellanas"),
#)
  
# creating a form 
class InteresFormulario(ModelForm):
    class Meta:
     model = Interes1 
     fields=("opcion",)
     
    