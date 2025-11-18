from django.urls import path, re_path
from alunos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('lista/', views.lista, name='lista'),
    path('new/', views.novo_aluno, name='novo_aluno'),
    path('total/', views.dashboard, name='dashboard'),
    path('edite/<int:id>', views.editar, name='edite'),
    path('actualizar/<int:id>', views.actualizar, name='actualizar'),
    path('mostrar/<int:id>', views.mostrar, name='mostrar'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('buscar/', views.abaBusca, name='abaBusca'),
    path('busca/', views.buscar, name='busca'),
    path('propina/<int:id>', views.propina, name='propina'),
    path('pagar/', views.pagar_propina, name='pagar'),
    path('registro/', views.abaLogin, name='login'),
    path('registro/', views.registro, name='registro.post'),
    path('registro/', views.abaRegistro, name='registro'),
    path('login/', views.login_users, name='login.post'),
    path('logout/', views.logout_users, name='logout'),
    path('movimento/', views.movimentos, name='movimento'),
    path('buscaturma/', views.abaturmas, name='abaTurma'),
    path('turma/', views.turmas, name='turma'),
    path('sala/', views.criar_sala, name='salas'),
    path('curso/', views.criar_curso, name='cursos'),
    path('pagas/<int:id>', views.propina_pagas, name='pagas'),
]