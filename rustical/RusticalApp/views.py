from django.shortcuts import render
from django.http import HttpResponse

from RusticalApp.models import usuario1
from RusticalApp.models import Interes1
from RusticalApp.models import compra1
from django.core import serializers

from RusticalApp.forms import UsuarioFormulario
from RusticalApp.forms import CompraFormulario
from RusticalApp.forms import InteresFormulario


def buscar(request):
    #Busqueda demanera filtrada
    Nombre=request.GET['Nombre']
    usuario_Todos=usuario1.objects.filter(Nombre=Nombre)
    return render(request,"RusticalApp/resultadoUsuario.html",{"Nombre":Nombre,"usuarios":usuario_Todos})
    

def buscarusuario(request):
    return render(request,'RusticalApp/busquedaUsuario.html')

def inicio(request):
    return render(request,'RusticalApp/inicio.html')

def usuario(request):
    if request.method == "POST":
        miFormulario = UsuarioFormulario(request.POST) # Aqui me llega la informacion del html            
        print(miFormulario)               
    
        if miFormulario.is_valid:                   
             informacion = miFormulario.cleaned_data                   
             familia = usuario1(Nombre=informacion["Nombre"], Apellidos=informacion["Apellidos"], Edad=informacion["Edad"])                  
             familia.save()                   
             return render(request, "RusticalApp/inicio.html")       
    else:             
        miFormulario = UsuarioFormulario()
 
    return render(request, "RusticalApp/usuario.html", {"miFormulario": miFormulario})
           


def Interes(request):
    if request.method == "POST":
        miFormulario2 = InteresFormulario(request.POST) # Aqui me llega la informacion del html            
        print(miFormulario2)               
    
        if miFormulario2.is_valid:                   
             informacion = miFormulario2.cleaned_data
             print(informacion)                   
             familia2 = Interes1(opcion=informacion['opcion'])
             familia2.save()                   
             return render(request, "RusticalApp/inicio.html")       
    else:             
        miFormulario2 = InteresFormulario()
 
    return render(request, "RusticalApp/interes.html", {"miFormulario2": miFormulario2})
    

   
    

def compra(request):
    if request.method == "POST":
        miFormulario1 = CompraFormulario(request.POST) # Aqui me llega la informacion del html            
        print(miFormulario1)               
    
        if miFormulario1.is_valid:                   
             informacion = miFormulario1.cleaned_data                   
             familia1 = compra1(Peso=informacion["Peso"], Unidades=informacion["Unidades"])                  
             familia1.save()                   
             return render(request, "RusticalApp/inicio.html")       
    else:             
        miFormulario1 = CompraFormulario()
 
    return render(request, "RusticalApp/compra.html", {"miFormulario1": miFormulario1})
    

def usuarioapi(request):
    usuario_todos=usuario1.objects.all()
    return HttpResponse(serializers.serialize('json',usuario_todos))     #Esto lo vuelve tipo diccionario
def Interesapi(request):
    Interes_todos=Interes1.objects.all()
    return HttpResponse(serializers.serialize('json',Interes_todos))    

def calcular(request):
    return render(request, "RusticalApp/calcularArea.html")

def area(request):
    x = request.GET["lado"]
    return render(request, "RusticalApp/resultado_area.html", {"area": round(25.325*float(x),0)})    

def read_user(request):
    usuario_all=usuario1.objects.all()
    return HttpResponse(serializers.serialize('json',usuario_all))

def create_user(request): 
    new_user=usuario1(Nombre='Nuevo_usuario', Apellidos='Apellido_nu', Edad=20)
    new_user.save()
    return HttpResponse(f'Usuario {new_user.Nombre} ha sido creado')

def edit_user(request):
    new_query='Nuevo_usuario'
    usuario1.objects.filter(Nombre=new_query).update(Nombre='Update_usuario')
    return HttpResponse(f'Usuario {new_query} ha sido actualizado')     

def erase_user(request):
    to_purge='Update_usuario'
    new_user=usuario1.objects.get(Nombre=to_purge)
    new_user.delete()
    return HttpResponse(f'Usuario {to_purge} ha sido eliminado')  


#vamos a crear una vista de todos los cursos
# Voy a crear una clase     
from django.views.generic import ListView #clase que permite listar
from django.views.generic.edit import CreateView,UpdateView,DeleteView #clases que me permiten crear, editar y borrar
class UserList(ListView):#Userlist va a heredar a Listview
    model=usuario1
    template='RusticalApp/usuario1_list.html'

 #CRUD  CREATE,READ, UPDATE, DELETE   


class UserCreate(CreateView):#Userlist va a heredar a Listview
    model=usuario1
    fields='__all__'
    success_url='/RusticalApp/user/list/'
   # template='RusticalApp/usuario1_list.html'

class UserEdit(UpdateView):
    model=usuario1
    fields='__all__'
    success_url='/RusticalApp/user/list/'

from django.views.generic.detail import DetailView

class UserDetail(DetailView):#Userlist va a heredar a Listview
    model=usuario1
    template='RusticalApp/usuario1_detail.html'   

class UserDelete(DeleteView):#Userlist va a heredar a Listview
    model=usuario1
    #fields='__all__'
    success_url='/RusticalApp/user/list/'   

def about(request):
    return render(request,'RusticalApp/about_us.html')     

def compraapi(request):
    compra_todos=compra1.objects.all()
    return HttpResponse(serializers.serialize('json',compra_todos))     #Esto lo vuelve tipo diccionario

class BuyList(ListView):#Userlist va a heredar a Listview
    model=compra1
    template='RusticalApp/compra1_list.html'

class BuyCreate(CreateView):#Userlist va a heredar a Listview
    model=compra1
    fields='__all__'
    success_url='/RusticalApp/buy/list/'

class BuyEdit(UpdateView):
    model=compra1
    fields='__all__'
    success_url='/RusticalApp/buy/list/'

class BuyDetail(DetailView):#Userlist va a heredar a Listview
    model=compra1
    template='RusticalApp/compra1_detail.html' 

class BuyDelete(DeleteView):#Userlist va a heredar a Listview
    model=compra1
    #fields='__all__'
    success_url='/RusticalApp/buy/list/' 

class InterestList(ListView):#Userlist va a heredar a Listview
    model=Interes1
    template='RusticalApp/Interes1_list.html'

class InterestCreate(CreateView):#Userlist va a heredar a Listview
    model=Interes1
    fields='__all__'
    success_url='/RusticalApp/interest/list/'    

class InterestEdit(UpdateView):
    model=Interes1
    fields='__all__'
    success_url='/RusticalApp/interest/list/'    

class InterestDetail(DetailView):#Userlist va a heredar a Listview
    model=Interes1
    template='RusticalApp/Interes1_detail.html'    

class InterestDelete(DeleteView):#Userlist va a heredar a Listview
    model=Interes1
    #fields='__all__'
    success_url='/RusticalApp/interest/list/' 

def contact(request):
    return render(request,'RusticalApp/contact.html')     