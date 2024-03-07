from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def home(request):
    return render(request, 'app/index.html')

def producto(request):
    contexto = {'productos': Libro.objects.all(), 'comentarios': Comentario.objects.all()}
    return render(request, 'app/producto.html', contexto)


def libro_form(request):
    if request.method == "POST":
        miFormulario = LibroForm(request.POST)
        if miFormulario.is_valid():
            libro_titulo = miFormulario.cleaned_data.get("titulo")
            libro_autor = miFormulario.cleaned_data.get("autor")
            libro_precio = miFormulario.cleaned_data.get("precio")
            libro_genero = miFormulario.cleaned_data.get("genero")
            libro_celContacto = miFormulario.cleaned_data.get("celContacto")
            libro_emailContacto = miFormulario.cleaned_data.get("emailContacto")
            libro = Libro(titulo=libro_titulo, autor=libro_autor, precio=libro_precio, genero=libro_genero, celContacto = libro_celContacto, emailContacto=libro_emailContacto)
            libro.save()

            contexto = {'productos': Libro.objects.all(), 'comentarios': Comentario.objects.all()}
            return render(request, "app/producto.html", contexto) 

    else:
        miFormulario = LibroForm()
        contexto = {"form": miFormulario}
    return render(request, "app/agregar_producto.html", contexto)

def coment_form(request):
    if request.method == "POST":
        miFormulario = ComentarioForm(request.POST)
        if miFormulario.is_valid():
            coment_texto = miFormulario.cleaned_data.get("texto")
            coment_usuario = miFormulario.cleaned_data.get("usuario")
            coment = Comentario(texto=coment_texto, usuario=coment_usuario)
            coment.save()

            contexto = {'productos': Libro.objects.all(), 'comentarios': Comentario.objects.all()}
            return render(request, "app/producto.html", contexto) 

    else:
        miFormulario = ComentarioForm()
        contexto = {"form": miFormulario}
    return render(request, "app/agregar_coment.html", contexto)

def usuario_form(request):
    if request.method == "POST":
        miFormulario = UsuarioForm(request.POST)
        if miFormulario.is_valid():
            usuario_nombre = miFormulario.cleaned_data.get("nombre")
            usuario_apellido = miFormulario.cleaned_data.get("apellido")
            usuario_email = miFormulario.cleaned_data.get("email")
            usuario_contraseña = miFormulario.cleaned_data.get("contraseña")
            usuario = Usuario(nombre=usuario_nombre, apellido=usuario_apellido, email=usuario_email, contraseña=usuario_contraseña)
            usuario.save()

            return render(request, "app/index.html") 

    else:
        miFormulario = UsuarioForm()
        contexto = {"form": miFormulario}
    return render(request, "app/agregar_usuario.html", contexto)

""" def buscarLibro(request):
    return render(request, "app/buscar_libro.html") """

def encontrarLibro(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        libros = Libro.objects.filter(titulo__icontains=patron)
        contexto = {"productos": libros, 'comentarios': Comentario.objects.all()}
        return render(request, "app/producto.html", contexto)
    

    contexto = {'productos': Libro.objects.all(), 'comentarios': Comentario.objects.all()}
    return render(request, "app/producto.html", contexto) 