from django.test import TestCase, Client
from .models import Alunos, Cursos, Salas, Propinas, Mensalidade, Usuario
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import Formulario_Cadastro

# Testando os models
class ModelsTestCase(TestCase):
 
    def setUp(self):
        self.curso = Cursos.objects.create(
            nome = 'Programação',
            tipo = 'Politécnico'
        )

        self.sala = Salas.objects.create(
            numero_sala = 10,
            descricao = 'Sala 10'
        )

        self.aluno = Alunos.objects.create(
            nome = 'Lionel André',
            data_nascimento = '2005-03-01',
            genero = 'M',
            tell = 948972536,
            classe = 13,
            sala = self.sala,
            turno = 'Tarde',
            curso = self.curso,
            turma = 'B'
        )

        self.mensalidade = Mensalidade.objects.create(
            curso = self.curso,
            classe = 10,
            mensalidade = 18000.00
        )

        self.propina = Propinas.objects.create(
            aluno = self.aluno,
            mes = 'Janeiro',
            preco = self.mensalidade
        )

    def test_aluno_criado(self):
        self.assertEqual(self.aluno.nome, 'Lionel André')
        self.assertEqual(self.aluno.data_nascimento, '2005-03-01')
        self.assertEqual(self.aluno.genero, 'M')
        self.assertEqual(self.aluno.tell, 948972536)
        self.assertEqual(self.aluno.classe, 13)
        self.assertEqual(self.aluno.sala.descricao, 'Sala 10')
        self.assertEqual(self.aluno.turno, 'Tarde')
        self.assertEqual(self.aluno.curso.nome, 'Programação')
        self.assertEqual(self.aluno.turma, 'B')

    def test_mensalidade_criado(self):
        self.assertEqual(self.mensalidade.curso.nome, 'Programação')
        self.assertEqual(self.mensalidade.classe, 10)
        self.assertEqual(self.mensalidade.mensalidade, 18000,00)

    def test_propina_criado(self):
        self.assertEqual(self.propina.aluno.nome, 'Lionel André')
        self.assertEqual(self.propina.mes, 'Janeiro')
        self.assertEqual(self.propina.preco.mensalidade, 18000,00)

    def test_str_representetion(self):
        self.assertEqual(str(self.aluno), 'Lionel André')
        self.assertEqual(str(self.propina), 'Janeiro')

# Testando as views 
class ViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.usuario = Usuario.objects.create_user(
            nome = 'Lionel André',
            email = 'lionelandre@gmail.com',
            username = 'LionelAndre',
            is_superuser = 1,
            password = 'lionel@01'
        )

    def setUp(self):
        self.client = Client()
        self.client.login(username='LionelAndre', password='lionel@01')

    def test_login(self):
        logged = self.client.login(username='LionelAndre', password='lionel@01')
        self.assertTrue(logged)

    def test_uma_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_cadastro_get(self):
        response = self.client.get(reverse('registro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aluno/registro.html')

    def test_cadastro_post(self):
        data = {
            'nome' : 'João Mateus',
            'email' : 'joaomateus@gmail.com',
            'username' : 'JoaoMateus',
            'password1' : 'lionel@01',
            'password2' : 'lionel@01'
        }
        response = self.client.post(reverse('registro'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aluno/registro.html')
        self.assertFalse(Usuario.objects.filter(username='JoaoMateus').exists())

    def test_cadastro_post_invalid_data(self):
        data = {
            'nome' : 'João Mateus',
            'email' : 'joaomateus@gmail.com',
            'username' : 'JoaoMateus',
            'password1' : 'lionel@01',
            'password2' : 'lionel@02'
        }
        response = self.client.post(reverse('registro'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aluno/registro.html')
        self.assertFalse(Usuario.objects.filter(username='JoaoMateus').exists())

    def test_cadastro_post_existing_username(self):
        Usuario.objects.create_user('JoaoMateus', 'joaomateus@gmail.com', 'lionel@01')
        data = {
            'nome' : 'João',
            'email' : 'joao@gmail.com',
            'username' : 'JoaoMateus',
            'password1' : 'lionel@02',
            'password2' : 'lionel@02'
        }
        response = self.client.post(reverse('registro.post'), data)
        self.assertNotEqual(response.status_code, 201)
        self.assertTemplateUsed(response, 'aluno/registro.html')
        self.assertEqual(Usuario.objects.filter(username='JoaoMateus').count(), 1)

    def test_novo_aluno(self):
        curso = Cursos.objects.create(
            nome = 'Programação',
            tipo = 'Politécnico'
        )
        
        sala = Salas.objects.create(
            numero_sala = 8,
            descricao = 'Sala de Programação'
        )

        dados = {
            'nome':'Lionel André',
            'curso': curso.id,
            'data_nascimento':'2005-03-01',
            'genero':'M',
            'turno':'Tarde',
            'classe': 13,
            'turma':'B',
            'tell':'948972536',
            'sala': sala.id
        }

        responsse = self.client.post(reverse('novo_aluno'), dados)
        self.assertEqual(responsse.status_code, 200)

    def test_novo_aluno_dados_inavlidos(self):
        curso = Cursos.objects.create(
            nome = 'Programação',
            tipo = 'Politécnico'
        )
        
        sala = Salas.objects.create(
            numero_sala = 8,
            descricao = 'Sala de Programação'
        )

        dados = {
            'nome':'Lionel André',
            'curso': curso.nome,
            'data_nascimento':'2005-03-01',
            'genero':'M',
            'turno':'Tarde',
            'classe': 13,
            'turma':'B',
            'tell':'948972536',
            'sala': sala.descricao
        }

        responsse = self.client.post(reverse('novo_aluno'), dados)
        self.assertEqual(responsse.status_code, 200)
        self.assertEqual(Alunos.objects.count(), 0)

    def test_editar_aluno(self):
        curso = Cursos.objects.create(
            nome = 'Programação',
            tipo = 'Politécnico'
        )
        
        salas = Salas.objects.create(
            numero_sala = 8,
            descricao = 'Sala de Programação'
        )

        aluno = Alunos.objects.create(
            nome = 'Lionel André',
            curso = curso,
            data_nascimento = '2005-03-01',
            genero = 'M',
            turno = 'Tarde',
            classe =  13,
            turma = 'B',
            tell = 948972536,
            sala = salas
        )

        url = reverse('edite', args=[aluno.id])

        dados_novos = {
            'nome':'Lionel Cristóvão',
            'curso': curso.id,
            'data_nascimento':'2010-03-01',
            'genero':'M',
            'turno':'Tarde',
            'classe': 13,
            'turma':'B',
            'tell':'948972536',
            'sala': salas.id
        }

        response = self.client.post(url, dados_novos)
        self.assertEqual(response.status_code, 200)

        aluno.refresh_from_db()
        self.assertEqual(aluno.nome, 'Lionel Cristóvão')
        self.assertEqual(aluno.data_nascimento, '2010-03-01')

    def tearDown(self):
        return print('Testes Bem Sucedidos')
    
class FormTestCase(TestCase):
    def setUp(self):
        self.dados_validos = {
            'nome':'Lionel',
            'curso':'Programação',
            'data_nascimento':'2005-03-01',
            'genero':'Masculino',
            'turno':'Tarde',
            'classe':'13ª Classe',
            'turma':'Turma B',
            'tell':'948972536',
            'sala':'Sala 8 - Programação (Turma B)'
        }

    def form_valido(self):
        form = Formulario_Cadastro(data=self.dados_validos)
        self.assertTrue(form.is_valid())

    def form_invalido(self):
        dados = self.dados_validos.copy()
        dados['nome'] = ''
        form = Formulario_Cadastro(data=dados)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)

    def tearDown(self):
        return print('Formulários Funcionais')