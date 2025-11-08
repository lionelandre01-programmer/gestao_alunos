from django.urls import path
from alunos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.lista, name='lista'),
    path('base/', views.novo_aluno, name='novo_aluno'),
    path('total/', views.dashboard, name='dashboard'),
    path('edite/<int:id>', views.editar, name='edite'),
    path('actualizar/<int:id>', views.actualizar, name='actualizar'),
    path('mostrar/<int:id>', views.mostrar, name='mostrar'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('buscar/', views.abaBusca, name='abaBusca'),
    path('busca/', views.buscar, name='busca'),
]