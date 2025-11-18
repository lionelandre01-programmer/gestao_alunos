from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse
from django.urls import reverse
from .models import Alunos
from .models import Salas
from .models import Cursos
from .forms import Formulario_Cadastro, PropinaForm
from .forms import EditeForm, RegistroForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from .models import Propinas
from .models import Movimentos
from django.contrib import messages

# Create your views here.
def index(request):
    """Página inicial do projecto"""
    sala = Salas.objects.all()
    curso = Cursos.objects.all()
    return render(request, 'aluno/index.html', {'sala' : sala, 'curso' : curso})

def lista(request):
    aluno = Alunos.objects.all()
    return render(request, 'aluno/lista.html', {'aluno' : aluno})

"""Cadastrando um novo aluno"""
def cadastro(request):
    form = Formulario_Cadastro()
    return render(request, 'aluno/cadastro.html', {'form' : form})

def novo_aluno(request):
    if request.method == 'POST':
        form = Formulario_Cadastro(request.POST)
        if form.is_valid():
            aluno = form.save()
            return render(request, 'aluno/cadastro.html', {'aluno' : aluno})
        else:
            print(form.errors)
            return render(request, 'aluno/cadastro.html', {'form' : form })
    else:
        form = Formulario_Cadastro()
        return render(request, 'aluno/cadastro.html', {'form' : form})
   
"""DashBoard Do Sistema"""
def dashboard(request):
    total = Alunos.objects.count()
    masculino = Alunos.objects.filter(genero = 'M').count()
    feminino = Alunos.objects.filter(genero = 'F').count()
    alunosEnfe = Alunos.objects.filter(curso = 6).count()
    alunosCont = Alunos.objects.filter(curso = 3).count()
    alunosProg = Alunos.objects.filter(curso = 1).count()
    alunosGE = Alunos.objects.filter(curso = 4).count()
    alunosElec = Alunos.objects.filter(curso = 5).count()
    alunosInfo = Alunos.objects.filter(curso = 2).count()
    alunosMa = Alunos.objects.filter(turno = 'Manhã').count()
    alunosTa = Alunos.objects.filter(turno = 'Tarde').count()
    
    return render(request, 'aluno/dashboard.html', 
                  {'total' : total, 
                   'totalM' : masculino, 
                   'totalF' : feminino, 
                   'totalEnfe' : alunosEnfe, 
                   'totalCont' : alunosCont, 
                   'totalProg' : alunosProg,
                   'totalGE' : alunosGE, 
                   'totalElec' : alunosElec, 
                   'totalInfo' : alunosInfo,
                   'totalMa' : alunosMa,
                   'totalTa' : alunosTa
                   })

"""Mostrar as informações do aluno"""
def mostrar(request, id):
    aluno = Alunos.objects.get(id = id)
    return render(request, 'aluno/mostrar.html', {'aluno' : aluno})

"""Editar e Actualizar dados do aluno"""
def editar(request, id):
    aluno = Alunos.objects.get(id = id)
    form = EditeForm(instance = aluno)
    return render(request, 'aluno/edite.html', {'form' : form})

def actualizar(request, id):
    if request.method == 'POST':
        aluno = Alunos.objects.get(id = id)
        form = EditeForm(request.POST, instance = aluno)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista'))
    else:
        return redirect(reverse('edite'))

"""Eliminar aluno"""
def delete(request, id):
    aluno = Alunos.objects.get(id=id)
    aluno.delete()
    return redirect(reverse('lista'))

"""Realizar busca de aluno pelo id ou nome"""
def abaBusca(request):
    return render(request,'aluno/busca.html')

def buscar(request):
    valorId = request.POST.get('buscaId')
    valorNome = request.POST.get('buscaNome')
    if valorId:
        idBusca = int(valorId)
        aluno = Alunos.objects.filter(id = idBusca).first()

        if not aluno:
            messages.error(request, 'Aluno não encontrado!')

    elif valorNome:
        nomeBusca = str(valorNome)
        aluno = Alunos.objects.filter(nome = nomeBusca).first()

        if not aluno:
            messages.error(request, 'Aluno não encontrado!')
            return render(request,'aluno/busca.html')
    else:
        aluno = Alunos.objects.none()

        if not aluno:
            messages.error(request, 'Preencha um dos campos!')
            return render(request,'aluno/busca.html', {'aluno' : aluno})

    return render(request,'aluno/busca.html', {'aluno' : aluno})

"""Realizar Pagamentos de propinas"""
def propina_pagas(request, id):
    propinas = Propinas.objects.filter(aluno_id = id)
    aluno = Alunos.objects.get(id=id)
    return render(request, 'aluno/pagas.html', {'propinas' : propinas, 'aluno' : aluno})

def propina(request, id):
    aluno = Alunos.objects.get(id=id)
    ultimo = Propinas.objects.filter(aluno = aluno).order_by('-id').first()
    return render(request, 'aluno/propina.html', {'aluno' : aluno, 'ultimo' : ultimo})

def pagar_propina(request):
    if request.method == 'POST':
        
        id = request.POST.get('aluno')
        mes = request.POST.get('mes')
        preco = request.POST.get('preco')
        aluno = Alunos.objects.get(id=id)
        propinas = Propinas.objects.filter(aluno_id = id)
        meses = []

        for propina in propinas:
            meses.append(propina.mes)

        if mes in meses:
            messages.error(request, f'O mês de {mes} já foi pago!')
            return redirect(reverse('abaBusca'))

        else:
            Propinas.objects.create(
                aluno = aluno,
                mes = mes,
                preco = preco
            ).save()

            messages.success(request, 'Propina Paga com sucesso!')
            return redirect(reverse('abaBusca'))
    
    else:
        messages.error(request, 'Falha no envio do formulário!')
        return redirect(reverse('abaBusca'))

"""Realizar as buscas de alunos por turmas"""
def abaturmas(request):
    return render(request, 'aluno/turma.html')

def turmas(request):
    classe = request.POST.get('classe')
    turma = request.POST.get('turma')
    turno = request.POST.get('turno')

    if classe and turma and turno:
        todos = Alunos.objects.filter(classe = classe, turma = turma, turno = turno)
        return render(request, 'aluno/turma.html', {'todos' : todos})

    else:
        messages.error(request, 'Preencha sempre o campo Classe!') 
        return render(request, 'aluno/turma.html')

"""Trazer todas as actividades que ocorrem no sistema"""
def movimentos(request):
    movimento = Movimentos.objects.all()
    return render(request, 'aluno/movimentos.html', {'movimento' : movimento})

"""Cadastro de um funcionário"""
def abaRegistro(request):
    form = RegistroForm()
    return render(request, 'aluno/registro.html', {'form' : form})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegistroForm()
        return render(request, 'aluno/registro.html', {'form' : form})

"""Fazer login"""
def abaLogin(request):
    form = LoginForm()
    return render(request, 'aluno/login.html', {'form' : form})

def login_users(request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('index')

    else:
        form = LoginForm()
        return render(request, 'aluno/login.html', {'form' : form})

def logout_users(request):
    logout(request)
    return redirect('index')       

"""Preencher a tabela Salas"""
def criar_sala(request):
    Sala = [
        'Sala 1 - Enfermagem (Turma A)',
        'Sala 2 - Programação (Turma A)',
        'Sala 3 - Informática (Turma A)',
        'Sala 4 - Contabilidade (Turma A)',
        'Sala 5 - Gestão de Empresas (Turma A)',
        'Sala 6 - Electricidade (Turma A)',
        'Sala 7 - Enfermagem (Turma B)',
        'Sala 8 - Programação (Turma B)',
        'Sala 9 - Informática (Turma B)',
        'Sala 10 - Contabilidade (Turma B)',
        'Sala 11 - Gestão de Empresas (Turma B)',
        'Sala 12 - Electricidade (Turma B)',
        'Sala 13 - Enfermagem (Turma C)',
        'Sala 14 - Programação (Turma C)',
        'Sala 15 - Informática (Turma C)',
        'Sala 16 - Contabilidade (Turma C)',
        'Sala 17 - Gestão de Empresas (Turma C)',
        'Sala 18 - Electricidade (Turma C)',
        'Sala 19 - Enfermagem (Turma D)',
        'Sala 20 - Programação (Turma D)',
        'Sala 21 - Informática (Turma D)',
        'Sala 22 - Contabilidade (Turma D)',
        'Sala 23 - Gestão de Empresas (Turma D)',
        'Sala 24 - Electricidade (Turma D)'
        ]

    for i in range(0,24):
        Salas.objects.create(numero_sala = i, descricao = Sala[i])
    
    messages.success(request, 'Salas criadas com sucesso!')
    return redirect(reverse('index'))

"""Preencher a tabela Cursos"""
def criar_curso(request):
    Tipo = [
        'Politécnico',
        'Saúde'
    ]

    Curso = [
        'Enfermagem',
        'Programação',
        'Informática',
        'Contabilidade',
        'Gestão Empresarial',
        'Electricidade'
    ]

    for i in range(1,6):
        Cursos.objects.create( nome = Curso[i], tipo = Tipo[0])

    Cursos.objects.create( nome = Curso[0], tipo = Tipo[1])

    messages.success(request, 'Cursos criados com sucesso!')
    return redirect(reverse('index'))