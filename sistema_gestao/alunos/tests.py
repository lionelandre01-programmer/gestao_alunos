from django.test import TestCase, Client
from .models import Alunos, Cursos, Salas, Propinas, Mensalidade
from django.urls import reverse

# Create your tests here.
class AlunoTestCase(TestCase):
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

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_uma_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)