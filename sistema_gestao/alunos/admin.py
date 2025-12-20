from django.contrib import admin
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from .models import Alunos, Pagamentos, Professores, Cursos, Salas, Usuario, Mensalidade, Disciplinas, Notas, Propinas, Movimentos

    # Register your models here.
def grupos():
    """Criação de grupos"""
    grupo_admin, criado_admin = Group.objects.get_or_create(name='Administradores')
    grupo_gest, criado_gest = Group.objects.get_or_create(name='Gestores')
    grupo_secret, criado_secret = Group.objects.get_or_create(name='Secretarios')
    grupo_prof, criado_prof = Group.objects.get_or_create(name='Professores')

    """Identificando o conteúdo para uma tabela"""
    content_type_aluno = ContentType.objects.get_for_model(Alunos)
    content_type_pagamento = ContentType.objects.get_for_model(Pagamentos)
    content_type_professor = ContentType.objects.get_for_model(Professores)
    content_type_curso = ContentType.objects.get_for_model(Cursos)
    content_type_sala = ContentType.objects.get_for_model(Salas)
    content_type_usuario = ContentType.objects.get_for_model(Usuario)
    content_type_mensalidade = ContentType.objects.get_for_model(Mensalidade)
    content_type_disciplina = ContentType.objects.get_for_model(Disciplinas)
    content_type_nota = ContentType.objects.get_for_model(Notas)
    content_type_propina = ContentType.objects.get_for_model(Propinas)
    content_type_movimento = ContentType.objects.get_for_model(Movimentos)

    """Permissões em alunos"""
    add_aluno = Permission.objects.get(codename='add_alunos', content_type=content_type_aluno)
    change_aluno = Permission.objects.get(codename='change_alunos', content_type=content_type_aluno)
    view_aluno = Permission.objects.get(codename='view_alunos', content_type=content_type_aluno)
    delete_aluno = Permission.objects.get(codename='delete_alunos', content_type=content_type_aluno)

    """Permissões em pagamentos"""
    add_pagamento = Permission.objects.get(codename='add_pagamentos', content_type=content_type_pagamento)
    change_pagamento = Permission.objects.get(codename='change_pagamentos', content_type=content_type_pagamento)
    view_pagamento = Permission.objects.get(codename='view_pagamentos', content_type=content_type_pagamento)
    delete_pagamento = Permission.objects.get(codename='delete_pagamentos', content_type=content_type_pagamento)

    """Permissões em professores"""
    add_professor = Permission.objects.get(codename='add_professores', content_type=content_type_professor)
    change_professor = Permission.objects.get(codename='change_professores', content_type=content_type_professor)
    view_professor = Permission.objects.get(codename='view_professores', content_type=content_type_professor)
    delete_professor = Permission.objects.get(codename='delete_professores', content_type=content_type_professor)

    """Permissões em cursos"""
    add_curso = Permission.objects.get(codename='add_cursos', content_type=content_type_curso)
    change_curso = Permission.objects.get(codename='change_cursos', content_type=content_type_curso)
    view_curso = Permission.objects.get(codename='view_cursos', content_type=content_type_curso)
    delete_curso = Permission.objects.get(codename='delete_cursos', content_type=content_type_curso)

    """Permissões em salas"""
    add_sala = Permission.objects.get(codename='add_salas', content_type=content_type_sala)
    change_sala = Permission.objects.get(codename='change_salas', content_type=content_type_sala)
    view_sala = Permission.objects.get(codename='view_salas', content_type=content_type_sala)
    delete_sala = Permission.objects.get(codename='delete_salas', content_type=content_type_sala)

    """Permissões em usuarios"""
    add_usuario = Permission.objects.get(codename='add_usuario', content_type=content_type_usuario)
    change_usuario = Permission.objects.get(codename='change_usuario', content_type=content_type_usuario)
    view_usuario = Permission.objects.get(codename='view_usuario', content_type=content_type_usuario)
    delete_usuario = Permission.objects.get(codename='delete_usuario', content_type=content_type_usuario)

    """Permissão em mensalidades"""
    add_mensalidade = Permission.objects.get(codename='add_mensalidade', content_type=content_type_mensalidade)
    change_mensalidade = Permission.objects.get(codename='change_mensalidade', content_type=content_type_mensalidade)
    view_mensalidade = Permission.objects.get(codename='view_mensalidade', content_type=content_type_mensalidade)
    delete_mensalidade = Permission.objects.get(codename='delete_mensalidade', content_type=content_type_mensalidade)

    """Permissão em disciplina"""
    add_disciplina = Permission.objects.get(codename='add_disciplinas', content_type=content_type_disciplina)
    change_disciplina = Permission.objects.get(codename='change_disciplinas', content_type=content_type_disciplina)
    view_disciplina = Permission.objects.get(codename='view_disciplinas', content_type=content_type_disciplina)
    delete_disciplina = Permission.objects.get(codename='delete_disciplinas', content_type=content_type_disciplina)

    """Permissão em notas"""
    add_nota = Permission.objects.get(codename='add_notas', content_type=content_type_nota)
    change_nota = Permission.objects.get(codename='change_notas', content_type=content_type_nota)
    view_nota = Permission.objects.get(codename='view_notas', content_type=content_type_nota)
    delete_nota = Permission.objects.get(codename='delete_notas', content_type=content_type_nota)

    """Permissões em propina"""
    add_propina = Permission.objects.get(codename='add_propinas', content_type=content_type_propina)
    change_propina = Permission.objects.get(codename='change_propinas', content_type=content_type_propina)
    view_propina = Permission.objects.get(codename='view_propinas', content_type=content_type_propina)
    delete_propina = Permission.objects.get(codename='delete_propinas', content_type=content_type_propina)

    """Permissões em movimentos"""
    add_movimento = Permission.objects.get(codename='add_movimentos', content_type=content_type_movimento)
    change_movimento = Permission.objects.get(codename='change_movimentos', content_type=content_type_movimento)
    view_movimento = Permission.objects.get(codename='view_movimentos', content_type=content_type_movimento)
    delete_movimento = Permission.objects.get(codename='delete_movimentos', content_type=content_type_movimento)

    """Atribuindo permissões por grupo"""
    """Administradores"""
    grupo_admin.permissions.set([
        add_aluno, change_aluno, view_aluno, delete_aluno,
        add_pagamento, change_pagamento, view_pagamento, delete_pagamento,
        add_professor, change_professor, view_professor, delete_professor,
        add_curso, change_curso, view_curso, delete_curso,
        add_sala, change_sala, view_sala, delete_sala,
        add_usuario, change_usuario, view_usuario, delete_usuario,
        add_mensalidade, change_mensalidade, view_mensalidade, delete_mensalidade,
        add_disciplina, change_disciplina, view_disciplina, delete_disciplina,
        add_nota, change_nota, view_nota, delete_nota,
        add_propina, change_propina, view_propina, delete_propina,
        add_movimento, delete_movimento, change_movimento, view_movimento, delete_mensalidade
    ])

    """Gestores"""
    grupo_gest.permissions.set([
        add_aluno, change_aluno, view_aluno, delete_aluno,
        add_pagamento, change_pagamento, view_pagamento, delete_pagamento,
        add_professor, change_professor, view_professor, delete_professor,
        add_curso, change_curso, view_curso, delete_curso,
        add_sala, change_sala, view_sala, delete_sala,
        add_usuario, change_usuario, view_usuario, delete_usuario,
        add_mensalidade, change_mensalidade, view_mensalidade, delete_mensalidade,
        add_disciplina, change_disciplina, view_disciplina, delete_disciplina,
        add_propina, change_propina, view_propina, delete_propina,
        add_movimento, view_movimento
    ])

    """Secretárias"""
    grupo_secret.permissions.set([
        add_aluno, view_aluno,
        add_pagamento, view_pagamento,
        add_professor, view_professor,
        add_curso, view_curso,
        add_sala, view_sala,
        add_mensalidade, view_mensalidade,
        add_propina
    ])

    """Professores"""
    grupo_prof.permissions.set([
        view_aluno,view_professor,view_curso,view_sala,
        add_nota, change_nota, view_nota, delete_nota
    ])