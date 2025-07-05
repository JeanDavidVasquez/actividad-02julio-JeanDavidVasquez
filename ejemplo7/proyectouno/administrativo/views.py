from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.db.models import Sum
from django.db import models
# importar las clases de models.py
from administrativo.models import Matricula, Estudiante
from administrativo.forms import MatriculaForm, MatriculaEditForm
from administrativo.models import Matricula, Estudiante, Modulo
from administrativo.forms import MatriculaForm, MatriculaEditForm, ModuloForm, EstudianteForm

# vista que permita presesentar las matriculas
# el nombre de la vista es index.

def index(request):
    """
    """
    matriculas = Matricula.objects.all()

    titulo = "Listado de matriculas"
    informacion_template = {'matriculas': matriculas,
    'numero_matriculas': len(matriculas), 'mititulo': titulo}
    return render(request, 'index.html', informacion_template)


def detalle_matricula(request, id):
    """

    """

    matricula = Matricula.objects.get(pk=id)
    informacion_template = {'matricula': matricula}
    return render(request, 'detalle_matricula.html', informacion_template)


def crear_matricula(request):
    """
    """
    if request.method=='POST':
        formulario = MatriculaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = MatriculaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_matricula.html', diccionario)

def editar_matricula(request, id):
    """
    """
    matricula = Matricula.objects.get(pk=id)
    print("----------matricula")
    print(matricula)
    print("----------matricula")
    if request.method=='POST':
        formulario = MatriculaEditForm(request.POST, instance=matricula)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = MatriculaEditForm(instance=matricula)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_matricula.html', diccionario)

def detalle_estudiante(request, id):
    """
    Vista para mostrar el detalle de un estudiante, incluyendo tipo y costo de matrículas.
    """
    estudiante = Estudiante.objects.get(pk=id)
    costo_matriculas = Matricula.objects.filter(estudiante=estudiante).aggregate(total=models.Sum('costo'))['total'] or 0
    informacion_template = {
        'e': estudiante,
        'tipo_estudiante': estudiante.get_tipo_estudiante_display(),
        'costo_matriculas': costo_matriculas,
    }
    return render(request, 'detalle_estudiante.html', informacion_template)



def crear_modulo(request):
    """
    Vista para crear un nuevo módulo.
    """
    if request.method == 'POST':
        formulario = ModuloForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index_modulos')
    else:
        formulario = ModuloForm()
    return render(request, 'crear_modulo.html', {'formulario': formulario})

def crear_estudiante(request):
    """
    Vista para crear un nuevo estudiante.
    """
    if request.method == 'POST':
        formulario = EstudianteForm(request.POST)
        if formulario.is_valid():
            estudiante = formulario.save()  # Guarda y obtiene el objeto
            return redirect('detalle_estudiante', id=estudiante.id)  # Redirige al detalle
    else:
        formulario = EstudianteForm()
    return render(request, 'crear_estudiante.html', {'formulario': formulario})

def indexEstudiantes(request):
    """
    Vista para mostrar el listado de estudiantes.
    """
    estudiantes = Estudiante.objects.all()
    titulo = "Listado de estudiantes"
    informacion_template = {
        'estudiantes': estudiantes,
        'numero_estudiantes': estudiantes.count(),
        'mititulo': titulo
    }
    return render(request, 'indexEstudiantes.html', informacion_template)

def indexModulos(request):
    modulos = Modulo.objects.all()
    lista_modulos = []
    for modulo in modulos:
        valor_total = Matricula.objects.filter(modulo=modulo).aggregate(total=models.Sum('costo'))['total'] or 0
        lista_modulos.append({
            'nombre': modulo.nombre,
            'valor_total': valor_total,
        })
    return render(request, 'indexModulos.html', {
        'mititulo': 'Listado de Módulos',
        'numero_modulos': len(lista_modulos),
        'modulos': lista_modulos
    })

# ver los módulos
#    nombre del módulp
#    valor de todas las matriculas del módulo    
# ver los estudiantes >> de los estudiantes debo visualizar:
#    nombre 
#    apellido
#    cedula
#    edad
#    tipo_estudiante 
#    costo de matriculas

# crear módulos
# crear estudiantes
