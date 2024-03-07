from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name= "home"),

    path('libros/', producto, name= "producto"),

    path('agregarusuario/', usuario_form, name= "agregar_usuario"),


    path('agregarlibro/', libro_form, name= "agregar_libro"),
    path('agregarcomentario/', coment_form, name= "agregar_comentario"),


    #path('buscarlibro/', buscarLibro, name="buscar_libro"),
    path('encontrarlibro/', encontrarLibro, name="encontrar_libro"),
]