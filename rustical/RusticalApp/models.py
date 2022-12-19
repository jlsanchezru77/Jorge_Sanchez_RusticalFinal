from django.db import models
#from model_utils import Choices
#from django.utils.translation import gettext as _


class usuario1(models.Model):
    Nombre=models.CharField(max_length=40)
    Apellidos=models.CharField(max_length=40)
    Edad=models.IntegerField()


ops=[
        ('Compra', ('Me interesa adquirir Orellanas')),
        ('Cultivo', ('Me interesa cultivar Orellanas')),
    ]     
class Interes1(models.Model):
    opcion=models.CharField(max_length=40, choices=ops,default='Hola')
    
    

class compra1(models.Model):
    Peso=models.IntegerField()
    Unidades=models.IntegerField()      
    
