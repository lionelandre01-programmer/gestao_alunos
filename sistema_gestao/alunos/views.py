from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from .models import Alunos, Professores, Disciplinas
from .models import Salas, Mensalidade, Pagamentos
from .models import Cursos, Notas, Usuario
from .forms import Formulario_Cadastro, MensalidadeForm, DisciplinaForm
from .forms import EditeForm, RegistroForm, LoginForm, ProfessorForm, NotaForm
from django.contrib.auth import login, authenticate, logout
from .models import Propinas
from .models import Movimentos, Mensalidade
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group

# Create your views here.
def index(request):
    """Página inicial do projecto"""
    sala = Salas.objects.all()
    curso = Cursos.objects.all()
    return render(request, 'aluno/index.html', {'sala' : sala, 'curso' : curso})

@login_required(login_url='/login/')
def lista(request):
    grupo = Group.objects.get(id=4)
    group_auth = request.user.groups.first()

    if group_auth != grupo:
        aluno = Alunos.objects.all()
        return render(request, 'aluno/lista.html', {'aluno' : aluno})
    else:
        return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')

"""Cadastrando um novo aluno"""
@login_required(login_url='/login/')
def cadastro(request):
    grupo = Group.objects.get(id=4)
    group_auth = request.user.groups.first()

    if group_auth != grupo:
        form = Formulario_Cadastro()
        return render(request, 'aluno/cadastro.html', {'form' : form})
    else:
        return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')
    

@login_required(login_url='/login/')
def novo_aluno(request):
    if request.method == 'POST':
        grupo = Group.objects.get(id=4)
        group_auth = request.user.groups.first()

        if group_auth != grupo:
            form = Formulario_Cadastro(request.POST)
            if form.is_valid():
                nome = form.cleaned_data['nome']
                aluno = form.save()

                if request.user.is_authenticated:
                    Movimentos.objects.create(
                    tipo = 'Novo aluno',
                    Aluno = nome,
                    funcionario = request.user.nome
                    )

                    Pagamentos.objects.create(
                        tipo = 'Matrícula',
                        valor = 9000.00,
                        funcionario = request.user.nome
                    )

                return render(request, 'aluno/cadastro.html', {'aluno' : aluno})
            else:
                print(form.errors)
                return render(request, 'aluno/cadastro.html', {'form' : form })
        else:
            return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')

    else:
        form = Formulario_Cadastro()
        return render(request, 'aluno/cadastro.html', {'form' : form})
   
"""DashBoard Do Sistema"""
@login_required(login_url='/login/')
def dashboard(request):
    grupo = Group.objects.get(id=4)
    group_auth = request.user.groups.first()

    if group_auth != grupo:
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
    else:
         return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')

"""Mostrar as informações do aluno"""
@login_required(login_url='/login/')
def mostrar(request, id):
    grupo = Group.objects.get(id=4)
    group_auth = request.user.groups.first()

    if group_auth != grupo:
        aluno = Alunos.objects.get(id = id)
        return render(request, 'aluno/mostrar.html', {'aluno' : aluno})
    else:
        return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')
    

"""Editar e Actualizar dados do aluno"""
@login_required(login_url='/login/')
@permission_required('change_aluno')
def editar(request, id):
    grupo_secret = Group.objects.get(id=3)
    grupo_prof = Group.objects.get(id=4)
    group_auth = request.user.groups.first()

    if group_auth != grupo_secret and group_auth != grupo_prof:
        aluno = Alunos.objects.get(id = id)
        form = EditeForm(instance = aluno)
        return render(request, 'aluno/edite.html', {'form' : form})
    else:
        return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')


@login_required(login_url='/login/')
def actualizar(request, id):
    if request.method == 'POST':
        grupo_secret = Group.objects.get(id=3)
        grupo_prof = Group.objects.get(id=4)
        group_auth = request.user.groups.first()

        if group_auth != grupo_secret and group_auth != grupo_prof:
            aluno = Alunos.objects.get(id = id)
            form = EditeForm(request.POST, instance = aluno)
            if form.is_valid():
                form.save()

                if request.user.is_authenticated:
                    Movimentos.objects.create(
                    tipo = 'Aluno Editado',
                    Aluno = aluno.nome,
                    funcionario = request.user.nome
                    )

                return redirect(reverse('lista'))
        else:
            return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')
    else:
        return redirect(reverse('edite'))

"""Eliminar aluno"""
@login_required(login_url='/login/')
def delete(request, id):
    aluno = Alunos.objects.get(id=id)
    grupo_secret = Group.objects.get(id=3)
    grupo_prof = Group.objects.get(id=4)
    group_auth = request.user.groups.first()

    if group_auth != grupo_secret and group_auth != grupo_prof:
        if request.user.is_authenticated:
            Movimentos.objects.create(
            tipo = 'Aluno Deletado',
            Aluno = aluno.nome,
            funcionario = request.user.nome
            )
                
        aluno.delete()

        return redirect(reverse('lista'))
    
    else:
        return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')

"""Realizar busca de aluno pelo id ou nome"""
@login_required(login_url='/login/')
@permission_required('view_aluno')
def abaBusca(request):
    return render(request,'aluno/busca.html')

@login_required(login_url='/login/')
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
@login_required(login_url='/login/')
@permission_required('view_propina')
def propina_pagas(request, id):
    propinas = Propinas.objects.filter(aluno_id = id)
    aluno = Alunos.objects.get(id=id)
    grupo_prof = Group.objects.get(id=4)
    group_auth = request.user.groups.first()

    if group_auth != grupo_prof:
        return render(request, 'aluno/pagas.html', {'propinas' : propinas, 'aluno' : aluno})
    else:
         return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')

@login_required(login_url='/login/')
@permission_required('view_propina')
def propina(request, id):
    grupo_prof = Group.objects.get(id=4)
    group_auth = request.user.groups.first()

    if group_auth != grupo_prof:
        aluno = Alunos.objects.get(id=id)
        ultimo = Propinas.objects.filter(aluno = aluno).order_by('-id').first()
        mensal = Mensalidade.objects.get(curso_id=aluno.curso_id, classe=aluno.classe)
        mensali = mensal
        return render(request, 'aluno/propina.html', {'aluno' : aluno, 'ultimo' : ultimo, 'mensali' : mensali})
        
    else:
         return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')

@login_required(login_url='/login/')
def pagar_propina(request):
    if request.method == 'POST':
        grupo_prof = Group.objects.get(id=4)
        group_auth = request.user.groups.first()

        if group_auth != grupo_prof:
        
            id = request.POST.get('aluno')
            mes = request.POST.get('mes')
            preco = request.POST.get('mensal')
            aluno = Alunos.objects.get(id=id)
            mensali = Mensalidade.objects.get(id=preco)
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
                    preco = mensali
                )

                if request.user.is_authenticated:
                    Movimentos.objects.create(
                    tipo = 'Propina Paga',
                    Aluno = aluno.nome,
                    funcionario = request.user.nome
                    )

                    Pagamentos.objects.create(
                        tipo = 'Propina',
                        mes = mes,
                        valor = mensali.mensalidade,
                        funcionario = request.user.nome
                    )

                    messages.success(request, 'Propina Paga com sucesso!')
                    return redirect(reverse('abaBusca'))
        else:
            return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')
    
    else:
        messages.error(request, 'Falha no envio do formulário!')
        return redirect(reverse('abaBusca'))

"""Realizar as buscas de alunos por turmas"""
@login_required(login_url='/login/')
def abaturmas(request):
    return render(request, 'aluno/turma.html')

@login_required(login_url='/login/')
def turmas(request):
    grupo_prof = Group.objects.get(id=4)
    group_auth = request.user.groups.first()

    if group_auth != grupo_prof:
        classe = request.POST.get('classe')
        turma = request.POST.get('turma')
        turno = request.POST.get('turno')

        if classe and turma and turno:
            todos = Alunos.objects.filter(classe = classe, turma = turma, turno = turno)
            return render(request, 'aluno/turma.html', {'todos' : todos})

        else:
            messages.error(request, 'Preencha sempre o campo Classe!') 
            return render(request, 'aluno/turma.html')
    else:
        return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')

"""Trazer todas as actividades que ocorrem no sistema"""
@login_required(login_url='/login/')
def movimentos(request):
    grupo_admin = Group.objects.get(id=1)
    group_auth = request.user.groups.first()

    if group_auth == grupo_admin:
        movimentos = Movimentos.objects.all()
        return render(request, 'aluno/movimentos.html', {'movimentos' : movimentos})
    else:
         return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')
    

"""Cadastro de um funcionário"""
def abaRegistro(request):
    if Usuario.objects.count() != 0:
        if request.user.is_authenticated:
            superuser = Usuario.objects.filter(is_superuser=1).exists()
            grupos = Group.objects.exclude(name='Administradores')
        else:
            return redirect(reverse('login'))
    else:
        superuser = False
        grupos = Group.objects.all()
    form = RegistroForm()
    return render(request, 'aluno/registro.html', {'form' : form, 'grupos' : grupos, 'superuser' : superuser})

def registro(request):
    if request.method == 'POST':
        grupo = request.POST.get('grupo')
        firstName = request.POST.get('first_name')
        lastName = request.POST.get('last_name')
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(id=grupo)
            user.groups.add(group)
            user.nome = firstName+' '+lastName
            user.save()
            nome = user.nome

            if request.user.is_authenticated:
                Movimentos.objects.create(
                tipo = 'Novo funcionário',
                Aluno = nome,
                funcionario = request.user.nome
                )
                return redirect(reverse('index'))

            return redirect(reverse('login'))
        
        else:
            print(form.errors)
            erros = {}
            for campo, erro in form.errors.items():
                erros[campo] =  erro

            messages.error(request, 'Escolha uma palavra passe forte com letras e números')
            return render(request,'aluno/registro.html', {'erros' : erros})

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

    else:
        form = LoginForm()
        return render(request, 'aluno/login.html', {'form' : form})


@login_required(login_url='/login/')
def logout_users(request):
    logout(request)
    return redirect('index')       

"""Preencher a tabela Salas"""
@login_required(login_url='/login/')
def criar_sala(request):
    
    grupo_admin = Group.objects.get(id=1)
    group_auth = request.user.groups.first()

    if group_auth == grupo_admin:
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
    else:
        return HttpResponseForbidden('<h1>Apenas O Administrador é autorizado Para prosseguir na Execução de Tal Acção</h1>')

"""Preencher a tabela Cursos"""
@login_required(login_url='/login/')
def criar_curso(request):
    grupo_admin = Group.objects.get(id=1)
    group_auth = request.user.groups.first()

    if group_auth != grupo_admin:
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
    else:
        return HttpResponseForbidden('<h1>Apenas o Administrador é autorizado Para prosseguir na Execução de Tal Acção</h1>')

"""Registrando Mensalidades"""
@login_required(login_url='/login/')
def mensal(request):
    grupo_prof = Group.objects.get(id=4)
    group_auth = request.user.groups.first()

    if group_auth != grupo_prof:
        cursos = Cursos.objects.all()
        return render(request, 'aluno/mensal.html', {'cursos' : cursos})
    else:
        return HttpResponseForbidden('<h1>Apenas Funcionários autorizados Podem Prosseguir com a Execução de Tal Acção</h1>')

@login_required(login_url='/login/')
def registro_mensalidade(request):
    if request.method == 'POST':
        grupo_prof = Group.objects.get(id=4)
        group_auth = request.user.groups.first()

        if group_auth != grupo_prof:
            form = MensalidadeForm(request.POST)

            if form.is_valid():
                if Mensalidade.objects.filter(curso=form.cleaned_data['curso'], mensalidade=form.cleaned_data['mensalidade']).exists():
                    messages.error(request, 'Mensalidade já registrada!')
                    return redirect(reverse('mensalidade'))
                
                else:
                    form.save()

                    if request.user.is_authenticated:
                        Movimentos.objects.create(
                        tipo = 'Mensalidade',
                        Aluno = 'WithOut',
                        funcionario = request.user.nome
                        )

                    messages.success(request, 'Mensalidade Cadastrada')
                    return HttpResponseRedirect(reverse('mensalidade'))
                
            else:
                messages.error(request, 'Formulário Inválido!')
                return redirect(reverse('mensalidade'))
        else:
            return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')
    
    else:
        form = MensalidadeForm()
        return render(request, 'aluno/mensal.html')
    
@login_required(login_url='/login/')
def mensalidades(request):
    grupo_prof = Group.objects.get(id=4)
    group_auth = request.user.groups.first()

    if group_auth != grupo_prof:
        mensalidades = Mensalidade.objects.all()

        if mensalidades:
            prog = Mensalidade.objects.filter(curso_id=1)
            info = Mensalidade.objects.filter(curso_id=2)
            cont = Mensalidade.objects.filter(curso_id=3)
            geEm = Mensalidade.objects.filter(curso_id=4)
            elec = Mensalidade.objects.filter(curso_id=5)
            enfe = Mensalidade.objects.filter(curso_id=6)
            return render(request, 'aluno/mensalidades.html', {
                'mensalidades' : mensalidades,
                'prog' : prog,
                'info' : info,
                'cont' : cont,
                'geEm' : geEm,
                'elec' : elec,
                'enfe' : enfe
                })
        
        else:
            messages.error(request, 'Sem Mensalidades!')
            return redirect(reverse('menslidades'))
    else:
        return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')

@login_required(login_url='/login/')
def disciplina(request):
    grupo_prof = Group.objects.get(id=4)
    group_auth = request.user.groups.first()

    if group_auth != grupo_prof:
        form = DisciplinaForm()
        return render(request, 'aluno/disciplinas.html', {'form' : form})
    else:
        return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')

@login_required(login_url='/login/')
def disciplinaSave(request):
    if request.method == 'POST':
        grupo_prof = Group.objects.get(id=4)
        group_auth = request.user.groups.first()

        if group_auth != grupo_prof:
            form = DisciplinaForm(request.POST)
            if form.is_valid():
                form.save()
                if request.user.is_authenticated:
                    Movimentos.objects.create(
                    tipo = 'Nova Disciplina',
                    Aluno = 'WithOut',
                    funcionario = request.user.nome
                )

                messages.success(request, 'Nova Disciplina Adicionada!')
                return redirect(reverse('disciplina'))
            
            else:
                messages.error(request, 'Formulário Inválido!')
                return redirect(reverse('disciplina'))
        else:
            return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')
    else:
        messages.warning(request, 'O formulário não foi enviado!')
        form = DisciplinaForm()
        return render(request, 'aluno/disciplinas.html', {'form' : form})

@login_required(login_url='/login/')
def professor(request):
    grupo_prof = Group.objects.get(id=4)
    group_auth = request.user.groups.first()

    if group_auth != grupo_prof:
        disciplinas = Disciplinas.objects.all()
        return render(request, 'aluno/professores.html', {'disciplinas' : disciplinas})
    else:
        return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')

@login_required(login_url='/login/')
def professorSave(request):
    if request.method == 'POST':
        grupo_prof = Group.objects.get(id=4)
        grupo_secret = Group.objects.get(id=3)
        group_auth = request.user.groups.first()

        if group_auth != grupo_prof and group_auth != grupo_secret:
            form = ProfessorForm(request.POST)
            if form.is_valid():
                nome = form.cleaned_data['nome']
                form.save()
                
                if request.user.is_authenticated:
                    Movimentos.objects.create(
                    tipo = 'Novo Professor',
                    Aluno = 'Prof. '+nome,
                    funcionario = request.user.nome
                )
                return redirect(reverse('professor'))    
                
            else:
                print(form.errors)
                erros = {}
                for campo, erro in form.errors.items():
                    erros[campo] =  erro

                return render(request, 'aluno/professores.html',{'erros':erros})
        else:
            return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')
    else:
        return redirect(reverse('professor'))
    
@login_required(login_url='/login/')
def nota(request):
    grupo_prof = Group.objects.get(id=4)
    grupo_admin = Group.objects.get(id=1)
    group_auth = request.user.groups.first()

    if group_auth == grupo_prof or group_auth == grupo_admin:
        professores = Professores.objects.all()
        alunos = Alunos.objects.all()
        disciplinas = Disciplinas.objects.all()
        return render(request, 'aluno/notas.html', {'professores' : professores, 'alunos' : alunos, 'disciplinas' : disciplinas})
    else:
        return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')

@login_required(login_url='/login/')
def notaSave(request):
    if request.method == 'POST':
        grupo_prof = Group.objects.get(id=4)
        grupo_admin = Group.objects.get(id=1)
        group_auth = request.user.groups.first()

        if group_auth == grupo_prof or group_auth == grupo_admin:
            form = NotaForm(request.POST)
            alunos = request.POST['aluno']
            if form.is_valid():
                form.save()
                alun = Alunos.objects.get(id=alunos)
                
                if request.user.is_authenticated:
                    Movimentos.objects.create(
                    tipo = 'Nota Preenchida',
                    Aluno = alun.nome,
                    funcionario = request.user.nome
                )
                return redirect(reverse('nota'))

            else:
                print(form.errors)
                erros = {}
                for campo, erro in form.errors.items():
                    erros[campo] =  erro

                return render(request, 'aluno/notas.html',{'erros':erros})
        else:
            return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')
    else:
        return redirect(reverse('professor'))
    
@login_required(login_url='/login/')
def financa(request):
    grupo_prof = Group.objects.get(id=4)
    group_auth = request.user.groups.first()

    if group_auth != grupo_prof:
        pagos = Pagamentos.objects.all()
        return render(request,'aluno/financa.html', {'pagos' : pagos})
    else:
        return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')
    
@login_required(login_url='/login/')
def pagamentos(request):
    grupo_prof = Group.objects.get(id=4)
    group_auth = request.user.groups.first()

    if group_auth != grupo_prof:
        totalpagos = Pagamentos.objects.aggregate(total = Sum('valor'))['total']
        propinas = Pagamentos.objects.filter(tipo='Propina').aggregate(prop = Sum('valor'))['prop']
        outros = Pagamentos.objects.exclude(tipo='Propina').aggregate(out = Sum('valor'))['out']
        return render(request, 'aluno/dadosfina.html', 
                    {
                        'totalpagos' : totalpagos,
                        'propinas' : propinas,
                        'outros' : outros
                    }
                    )
    else:
        return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')

@login_required(login_url='/login/')
def verNotas(request, id):
    grupo_prof = Group.objects.get(id=4)
    group_auth = request.user.groups.first()

    if group_auth != grupo_prof:
        notas = Notas.objects.filter(aluno_id=id)
        aluno = Alunos.objects.get(id=id)
        return render(request, 'aluno/notas_aluno.html', {'notas' : notas, 'aluno' : aluno})
    else:
        return HttpResponseForbidden('<h1>Apenas Funcionários Autorizados Podem prosseguir na Execução de Tal Acção</h1>')

def verFuncionario(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, 'aluno/funcionarios.html', {'usuario' : usuario})

def proximoFuncionario(request, id):
    valor = id+1
    if Usuario.objects.filter(id=valor).exists():
        usuario = Usuario.objects.get(id=valor)
        return render(request, 'aluno/funcionarios.html', {'usuario' : usuario})
    else:
        usuario = Usuario.objects.get(id=id)
        return render(request, 'aluno/funcionarios.html', {'usuario' : usuario})
    
"""OBS: password: louerna@05"""
