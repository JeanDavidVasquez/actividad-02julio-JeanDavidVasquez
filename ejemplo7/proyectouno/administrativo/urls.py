from django.urls import path
# se importa las vistas de la aplicación
from administrativo import views

urlpatterns = [
        path('', views.index, name='index'),
        path('detalle/matricula/<int:id>', views.detalle_matricula,
            name='detalle_matricula'),

        path('crear/nueva/matricula', views.crear_matricula,
            name='crear_matricula'),

        path('editar/matricula/<int:id>', views.editar_matricula,
                name='editar_matricula'),
        path('detalle/estudiante/<int:id>', views.detalle_estudiante,
            name='detalle_estudiante'),
        path('indexEstudiantes/', views.indexEstudiantes, name='index_estudiantes'),

        path('crear_estudiante/', views.crear_estudiante, name='crear_estudiante'), 
          # Para crear estudiante
        path('crear_modulo/', views.crear_modulo, name='crear_modulo'),        
        path('indexModulos/', views.indexModulos, name='index_modulos'),   
             
        ]
        
        
        
 