from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect,get_object_or_404

from django.urls import reverse
from .forms import LibroForm, CompraForm, UserRegisterForm
from .models import Libro, Compra
#usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
#Inicio
def index(request):
    libros = Libro.objects.all()
    compras = Compra.objects.all()
    return render(request, 'crud/index.html', {'libro': libros, 'compras': compras})

#Base 
def base(request):
    return render(request, 'crud/base.html')
#Vista del libro
def view_libro(request,id):
    libro=Libro.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))
#Agregar
def add(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            nuevo_libro = form.cleaned_data['nombre']  
            nuevo_autor = form.cleaned_data['autor']
            nuevo_codigo = form.cleaned_data['codigo']

            nuevolibro = Libro(
                nombre=nuevo_libro,  
                autor=nuevo_autor,
                codigo=nuevo_codigo,
                estado='A'
            )

            nuevolibro.save()
            return render(request, 'crud/add.html', {
                'form': LibroForm(),
                'success': True
            })
        else:
            form = LibroForm()
    else:
        form = LibroForm()

    return render(request, 'crud/add.html', {
        'form': form,
    })
#editar
def edita(request, id):
    libro = Libro.objects.get(pk=id)

    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return render(request, 'crud/edit.html', {
                'form': form,
                'success': True
            })
    else:
        form = LibroForm(instance=libro)

    return render(request, 'crud/edit.html', {
        'form': form,
        'libro': libro
    })

#eliminar
def elimina(request, id):
    if request.method =='POST':
        libro = Libro.objects.get(pk=id)
        libro.delete()
    return HttpResponseRedirect(reverse('index'))
#compra
def compras(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Compra exitosa!')
            return redirect('index')
    else:
        form = CompraForm()

    context = {'form': form}
    return render(request, 'crud/compras.html', context)
#registrase

def registrar(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data["username"]
            user = form.save()
            login(request, user)
            messages.success(request, 'Tu cuenta ha sido creada exitosamente.')
            return redirect('index')
    else:
        form =UserRegisterForm()
    contex = {'form': form}
    return render(request,'crud/register.html', contex)

