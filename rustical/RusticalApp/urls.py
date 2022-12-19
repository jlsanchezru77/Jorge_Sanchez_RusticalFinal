from django.urls import path
from RusticalApp import views

urlpatterns = [
    path("",views.inicio,name='Inicio'),
    path('usuario1/', views.usuario,name='Usuario'),
    path('usuarioApi/', views.usuarioapi,name='userapi'),
    path('InteresApi/', views.Interesapi,name='interestapi'),
    path('Interes1/', views.Interes,name='Interes'),
    path('compra/', views.compra,name='Compra'),
    path('busquedaUsuario/',views.buscarusuario),
    path("calcular/", views.calcular,name='Calcular'),
    path("area/", views.area),
    path("buscar/",views.buscar),
    path("Leerusuario/",views.read_user),
    path("Crearusuario/",views.create_user),
    path("Editarusuario/",views.edit_user),
    path("Eliminarusuario/",views.erase_user),
    path("user/list/",views.UserList.as_view(),name='List'),#llamo el metodo asview
    path("user/create/", views.UserCreate.as_view(),name='New'),
    path("user/edit/<pk>", views.UserEdit.as_view(),name='Edit'), #el <pk> es el identificador unico de la url y sirve de argumento para editar
    path("user/detail/<pk>", views.UserDetail.as_view(),name='Detail'),
    path("user/delete/<pk>", views.UserDelete.as_view(),name='Delete'),
    path("about/",views.about,name='about'),
    path('compraApi/', views.compraapi,name='buyapi'),
    path("buy/list/",views.BuyList.as_view(),name='List1'),
    path("buy/create/", views.BuyCreate.as_view(),name='NewBuy'),
    path("buy/edit/<pk>", views.BuyEdit.as_view(),name='EditBuy'),
    path("buy/detail/<pk>", views.BuyDetail.as_view(),name='DetailBuy'),
    path("buy/delete/<pk>", views.BuyDelete.as_view(),name='DeleteBuy'),
    path("interest/list/",views.InterestList.as_view(),name='List2'),
    path("interest/create/", views.InterestCreate.as_view(),name='NewInterest'),
    path("interest/edit/<pk>", views.InterestEdit.as_view(),name='EditInterest'),
    path("interest/detail/<pk>", views.InterestDetail.as_view(),name='DetailI'),
    path("interest/delete/<pk>", views.InterestDelete.as_view(),name='DeleteI'),
    path("contact/",views.contact,name='contact')
]