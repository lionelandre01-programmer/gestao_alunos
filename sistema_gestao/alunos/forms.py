from django import forms
from .models import Alunos, Propinas, Mensalidade, Disciplinas, Professores, Notas
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

"""Formulário Para Cadastrar Alunos"""
class Formulario_Cadastro(forms.ModelForm):
    class Meta:
        model = Alunos
        fields = ('nome', 'curso', 'turma' ,'tell' ,'data_nascimento', 'genero', 'classe', 'sala', 'turno')

        widgets = {
            'nome' : forms.TextInput(attrs={ 'placeholder' : 'Nome do Aluno' }),
            'curso' : forms.Select(attrs={ 'placeholder' : 'Curso do Aluno', 'class' : 'genero' }, choices=[
                (6, 'Enfermagem'),
                (1, 'Programação'),
                (2, 'Informática'),
                (3, 'Contabilidade'),
                (4, 'Gestão de Empresas'),
                (5, 'Electricidade'),
            ]),
            'data_nascimento' : forms.DateInput(attrs={'type' : 'date'}),
            'genero' : forms.Select(attrs={ 'placeholder' : 'Genero do Aluno', 'class' : 'genero' }, choices=[
                ('M', 'Masculino'),
                ('F', 'Feminino'),
            ]),
            'turno' : forms.Select(attrs={ 'class' : 'genero' }, choices=[
                ('Manhã', 'Manhã'),
                ('Tarde', 'Tarde'),
            ]),
            'classe' : forms.Select(attrs={ 'class' : 'genero' }, choices=[
                (10, '10ª Classe'),
                (11, '11ª Classe'),
                (12, '12ª Classe'),
                (13, '13ª Classe')
            ]),

            'turma' : forms.Select(attrs={ 'class' : 'genero' }, choices=[
                ('A', 'Turma A'),
                ('B', 'Turm B'),
                ('C', 'Turma C'),
                ('D', 'Turma D')
            ]),

            'tell' : forms.NumberInput(attrs={ 'placeholder' : 'Seu Contacto' }),

            'sala' : forms.Select(attrs={ 'class' : 'genero' }, choices=[
                (1, 'Sala 1 - Enfermagem (Turma A)'),
                (2, 'Sala 2 - Programação (Turma A)'),
                (3, 'Sala 3 - Informática (Turma A)'),
                (4, 'Sala 4 - Contabilidade (Turma A)'),
                (5, 'Sala 5 - Gestão de Empresas (Turma A)'),
                (6, 'Sala 6 - Electricidade (Turma A)'),
                (7, 'Sala 7 - Enfermagem (Turma B)'),
                (8, 'Sala 8 - Programação (Turma B)'),
                (9, 'Sala 9 - Informática (Turma B)'),
                (10, 'Sala 10 - Contabilidade (Turma B)'),
                (11, 'Sala 11 - Gestão de Empresas (Turma B)'),
                (12, 'Sala 12 - Electricidade (Turma B)'),
                (13, 'Sala 7 - Enfermagem (Turma C)'),
                (14, 'Sala 8 - Programação (Turma C)'),
                (15, 'Sala 9 - Informática (Turma C)'),
                (16, 'Sala 10 - Contabilidade (Turma C)'),
                (17, 'Sala 11 - Gestão de Empresas (Turma C)'),
                (18, 'Sala 12 - Electricidade (Turma C)'),
                (19, 'Sala 13 - Enfermagem (Turma D)'),
                (20, 'Sala 14 - Programação (Turma D)'),
                (21, 'Sala 15 - Informática (Turma D)'),
                (22, 'Sala 16 - Contabilidade (Turma D)'),
                (23, 'Sala 17 - Gestão de Empresas (Turma D)'),
                (24, 'Sala 18 - Electricidade (Turma D)')
            ]),
        }

"""Formulário Para Editar Informações"""
class EditeForm(forms.ModelForm):
    class Meta:
        model = Alunos
        fields = ('nome', 'curso', 'turno', 'data_nascimento', 'genero', 'classe', 'sala')

        widgets = {
            'nome' : forms.TextInput(attrs={ 'placeholder' : 'Nome do Aluno' }),
            'curso' : forms.Select(attrs={ 'placeholder' : 'Curso do Aluno', 'class' : 'genero' }, choices=[
                ('Enfermagem', 'Enfermagem'),
                ('Programação', 'Programação'),
                ('Informática', 'Informática'),
                ('Contabilidade', 'Contabilidade'),
                ('Gestão Empresarial', 'Gestão de Empresas'),
                ('Electricidade', 'Electricidade'),
            ]),
            'data_nascimento' : forms.DateInput(attrs={'type' : 'date'}),
            'genero' : forms.Select(attrs={ 'class' : 'genero' }, choices=[
                ('M', 'Masculino'),
                ('F', 'Feminino'),
            ]),
            'turno' : forms.Select(attrs={ 'class' : 'genero' }, choices=[
                ('Manhã', 'Manhã'),
                ('Tarde', 'Tarde'),
            ]),
            'classe' : forms.Select(attrs={ 'class' : 'genero' }, choices=[
                ('10', '10ª Classe'),
                ('11', '11ª Classe'),
                ('12', '12ª Classe'),
                ('13', '13ª Classe'),
            ]),
            'sala' : forms.Select(attrs={ 'placeholder' : 'Sala do Aluno', 'class' : 'genero'}, choices=[
                ('1', 'Sala 1 - Enfermagem (10ª Manhã)'),
                ('2', 'Sala 2 - Programação (10ª Manhã)'),
                ('3', 'Sala 3 - Informática (10ª Manhã)'),
                ('4', 'Sala 4 - Contabilidade (10ª Manhã)'),
                ('5', 'Sala 5 - Gestão de Empresas (10ª Manhã)'),
                ('6', 'Sala 6 - Electricidade (10ª Manhã)'),
                ('7', 'Sala 7 - Enfermagem (11ª Manhã)'),
                ('8', 'Sala 8 - Programação (11ª Manhã)'),
                ('9', 'Sala 9 - Informática (11ª Manhã)'),
                ('10', 'Sala 10 - Contabilidade (11ª Manhã)'),
                ('11', 'Sala 11 - Gestão de Empresas (11ª Manhã)'),
                ('12', 'Sala 12 - Electricidade (11ª Manhã)'),
                ('13', 'Sala 13 - Enfermagem (12ª Manhã)'),
                ('14', 'Sala 14 - Programação (12ª Manhã)'),
                ('15', 'Sala 15 - Informática (12ª Manhã)'),
                ('16', 'Sala 16 - Contabilidade (12ª Manhã)'),
                ('17', 'Sala 17 - Gestão de Empresas (12ª Manhã)'),
                ('18', 'Sala 18 - Electricidade (12ª Manhã)'),
                ('19', 'Sala 19 - Enfermagem (13ª Manhã)'),
                ('20', 'Sala 20 - Programação (13ª Manhã)'),
                ('21', 'Sala 21 - Informática (13ª Manhã)'),
                ('22', 'Sala 22 - Contabilidade (13ª Manhã)'),
                ('23', 'Sala 23 - Gestão de Empresas (13ª Manhã)'),
                ('24', 'Sala 24 - Electricidade (13ª Manhã)'),
                ('1', 'Sala 1 - Enfermagem (10ª Tarde)'),
                ('2', 'Sala 2 - Programação (10ª Tarde)'),
                ('3', 'Sala 3 - Informática (10ª Tarde)'),
                ('4', 'Sala 4 - Contabilidade (10ª Tarde)'),
                ('5', 'Sala 5 - Gestão de Empresas (10ª Tarde)'),
                ('6', 'Sala 6 - Electricidade (10ª Tarde)'),
                ('7', 'Sala 7 - Enfermagem (11ª Tarde)'),
                ('8', 'Sala 8 - Programação (11ª Tarde)'),
                ('9', 'Sala 9 - Informática (11ª Tarde)'),
                ('10', 'Sala 10 - Contabilidade (11ª Tarde)'),
                ('11', 'Sala 11 - Gestão de Empresas (11ª Tarde)'),
                ('12', 'Sala 12 - Electricidade (11ª Tarde)'),
                ('13', 'Sala 13 - Enfermagem (12ª Tarde)'),
                ('14', 'Sala 14 - Programação (12ª Tarde)'),
                ('15', 'Sala 15 - Informática (12ª Tarde)'),
                ('16', 'Sala 16 - Contabilidade (12ª Tarde)'),
                ('17', 'Sala 17 - Gestão de Empresas (12ª Tarde)'),
                ('18', 'Sala 18 - Electricidade (12ª Tarde)'),
                ('19', 'Sala 19 - Enfermagem (13ª Tarde)'),
                ('20', 'Sala 20 - Programação (13ª Tarde)'),
                ('21', 'Sala 21 - Informática (13ª Tarde)'),
                ('22', 'Sala 22 - Contabilidade (13ª Tarde)'),
                ('23', 'Sala 23 - Gestão de Empresas (13ª Tarde)'),
                ('24', 'Sala 24 - Electricidade (13ª Tarde)'),
            ]),
        }

"""Formulário Para Registrar"""
class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nome', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update()
        self.fields['email'].widget.attrs.update()
        self.fields['nome'].widget.attrs.update()
        self.fields['password1'].widget.attrs.update()
        self.fields['password2'].widget.attrs.update()

"""Formulário Para Fazer o Login"""
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nome do usuário",
        widget=forms.TextInput(attrs={'class' : 'form-control'})
    )

    password = forms.CharField(
        label="Senha do usuário",
        widget=forms.PasswordInput(attrs={'class' : 'form-control'})
    )

"""Formulário Para As Propinas"""
class PropinaForm(forms.ModelForm):
    class Meta:
        model = Propinas
        fields = ('aluno', 'mes', 'preco')

        widgets = {
            'aluno' : forms.TextInput(attrs={'readonly' : 'readonly', 'class' : 'genero'}),

            'mes' : forms.DateInput(attrs={'type' : 'date',}),

            'preco' : forms.Select(attrs={'class' : 'genero'})
        }

class MensalidadeForm(forms.ModelForm):
    class Meta:
        model = Mensalidade
        fields = ('curso', 'classe', 'mensalidade')

        widgets = {
            'curso' : forms.TextInput(attrs={'readonly' : 'readonly'}),
            'classe' : forms.Select(attrs={'class' : 'genero'}, choices=[
                ('10', '10ª Classe'),
                ('11', '11ª Classe'),
                ('12', '12ª Classe'),
                ('13', '13ª Classe')
            ]),

            'mensalidade' : forms.Select(attrs={'class' : 'genero'}, choices=[
                (10000.00, '10.000,00kz'),
                (11000.00, '11.000,00kz'),
                (12000.00, '12.000,00kz'),
                (13000.00, '13.000,00kz'),
                (14000.00, '14.000,00kz'),
                (15000.00, '15.000,00kz'),
                (16000.00, '16.000,00kz'),
                (17000.00, '17.000,00kz'),
                (18000.00, '18.000,00kz'),
                (19000.00, '19.000,00kz'),
                (20000.00, '20.000,00kz')
            ]),
        }

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplinas
        fields = '__all__'

        widgets = { 'nome' : forms.TextInput() }
    

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professores
        fields = ('nome','sobrenome','disciplina','tempo_trabalho')

        widgets = {
            'nome' : forms.TextInput(attrs={'placeholder':'Seu nome'}),
            'sobrenome' : forms.TextInput(attrs={'placeholder':'Seu sobrenome'}),
            'disciplina' : forms.TextInput(attrs={'placeholder':'Disciplina que leciona'}),
            'tempo_trabalho' : forms.DateInput(attrs={'class':'genero'})
        }

class NotaForm(forms.ModelForm):
    class Meta:
        model = Notas
        fields = ('professor','aluno','disciplina','trimestre','prova','nota')

        widgets = {
            'professor' : forms.TextInput(),
            'aluno' : forms.TextInput(),
            'disciplina' : forms.TextInput(),
            'trimestre' : forms.Select(attrs={'class':'genero'}, choices= [
                ('1º'),
                ('2º'),
                ('3º')
            ]),
            'prova' : forms.Select(attrs={'class':'genero'}, choices= [
                ('Avaliação'),
                ('Prova do professor'),
                ('Prova Trimestral')
            ]),
            'nota' : forms.NumberInput()
        }