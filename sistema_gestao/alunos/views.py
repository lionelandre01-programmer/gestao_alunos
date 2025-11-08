from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from .models import Alunos
from .forms import Formulario_Cadastro
from .forms import EditeForm
from django.db.models import Q

# Create your views here.
def index(request):
    """Página inicial do projecto"""
    form = Formulario_Cadastro()
    return render(request, 'aluno/index.html', {'form' : form})

def lista(request):
    aluno = Alunos.objects.all()
    return render(request, 'aluno/lista.html', {'aluno' : aluno})

def novo_aluno(request):
    if request.method == 'POST':
        form = Formulario_Cadastro(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista'))
    else:
        form = Formulario_Cadastro()
        return render(request, 'aluno/indx.html', {'form' : form})


def dashboard(request):
    total = Alunos.objects.count()
    masculino = Alunos.objects.filter(genero = 'M').count()
    feminino = Alunos.objects.filter(genero = 'F').count()
    alunosEnfe = Alunos.objects.filter(curso = 'Enfermagem').count()
    alunosCont = Alunos.objects.filter(curso = 'Contabilidade').count()
    alunosProg = Alunos.objects.filter(curso = 'Programação').count()
    alunosGE = Alunos.objects.filter(curso = 'Gestão Empresarial').count()
    alunosElec = Alunos.objects.filter(curso = 'Electricidade').count()
    alunosInfo = Alunos.objects.filter(curso = 'Informática').count()
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

def mostrar(request, id):
    aluno = Alunos.objects.get(id = id)
    return render(request, 'aluno/mostrar.html', {'aluno' : aluno})

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

def delete(request, id):
    aluno = Alunos.objects.get(id=id)
    aluno.delete()
    return redirect(reverse('lista'))

def abaBusca(request):
    return render(request,'aluno/busca.html')

def buscar(request):
    valor = request.POST.get('busca')
    if valor:
        try:
            idBusca = int(valor)
            aluno = Alunos.objects.filter(id = idBusca)

        except ValueError:
            aluno = Alunos.objects.filter(nome_icontains = valor)

    else:
        aluno = Alunos.objects.none()
    
    return render(request,'aluno/busca.html', {'aluno' : aluno})