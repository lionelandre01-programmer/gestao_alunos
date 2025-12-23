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
    add_aluno, aluno1 = Permission.objects.get_or_create(codename='add_alunos', content_type=content_type_aluno)
    change_aluno, aluno2 = Permission.objects.get_or_create(codename='change_alunos', content_type=content_type_aluno)
    view_aluno, aluno3 = Permission.objects.get_or_create(codename='view_alunos', content_type=content_type_aluno)
    delete_aluno, aluno4 = Permission.objects.get_or_create(codename='delete_alunos', content_type=content_type_aluno)

    """Permissões em pagamentos"""
    add_pagamento, pagamento1 = Permission.objects.get_or_create(codename='add_pagamentos', content_type=content_type_pagamento)
    change_pagamento, pagamento2 = Permission.objects.get_or_create(codename='change_pagamentos', content_type=content_type_pagamento)
    view_pagamento, pagamento3 = Permission.objects.get_or_create(codename='view_pagamentos', content_type=content_type_pagamento)
    delete_pagamento, pagamento4 = Permission.objects.get_or_create(codename='delete_pagamentos', content_type=content_type_pagamento)

    """Permissões em professores"""
    add_professor, professor1 = Permission.objects.get_or_create(codename='add_professores', content_type=content_type_professor)
    change_professor, professor1 = Permission.objects.get_or_create(codename='change_professores', content_type=content_type_professor)
    view_professor, professor1 = Permission.objects.get_or_create(codename='view_professores', content_type=content_type_professor)
    delete_professor, professor1 = Permission.objects.get_or_create(codename='delete_professores', content_type=content_type_professor)

    """Permissões em cursos"""
    add_curso, curso1 = Permission.objects.get_or_create(codename='add_cursos', content_type=content_type_curso)
    change_curso, curso2 = Permission.objects.get_or_create(codename='change_cursos', content_type=content_type_curso)
    view_curso, curso3 = Permission.objects.get_or_create(codename='view_cursos', content_type=content_type_curso)
    delete_curso, curso4 = Permission.objects.get_or_create(codename='delete_cursos', content_type=content_type_curso)

    """Permissões em salas"""
    add_sala, sala1 = Permission.objects.get_or_create(codename='add_salas', content_type=content_type_sala)
    change_sala, sala2 = Permission.objects.get_or_create(codename='change_salas', content_type=content_type_sala)
    view_sala, sala3 = Permission.objects.get_or_create(codename='view_salas', content_type=content_type_sala)
    delete_sala, sala4 = Permission.objects.get_or_create(codename='delete_salas', content_type=content_type_sala)

    """Permissões em usuarios"""
    add_usuario, usuario1 = Permission.objects.get_or_create(codename='add_usuario', content_type=content_type_usuario)
    change_usuario, usuario2 = Permission.objects.get_or_create(codename='change_usuario', content_type=content_type_usuario)
    view_usuario, usuario3 = Permission.objects.get_or_create(codename='view_usuario', content_type=content_type_usuario)
    delete_usuario, usuario4 = Permission.objects.get_or_create(codename='delete_usuario', content_type=content_type_usuario)

    """Permissão em mensalidades"""
    add_mensalidade, mensalidade1 = Permission.objects.get_or_create(codename='add_mensalidade', content_type=content_type_mensalidade)
    change_mensalidade, mensalidade2 = Permission.objects.get_or_create(codename='change_mensalidade', content_type=content_type_mensalidade)
    view_mensalidade, mensalidade3 = Permission.objects.get_or_create(codename='view_mensalidade', content_type=content_type_mensalidade)
    delete_mensalidade, mensalidade4 = Permission.objects.get_or_create(codename='delete_mensalidade', content_type=content_type_mensalidade)

    """Permissão em disciplina"""
    add_disciplina, propina1 = Permission.objects.get_or_create(codename='add_disciplinas', content_type=content_type_disciplina)
    change_disciplina, propina2 = Permission.objects.get_or_create(codename='change_disciplinas', content_type=content_type_disciplina)
    view_disciplina, propina3 = Permission.objects.get_or_create(codename='view_disciplinas', content_type=content_type_disciplina)
    delete_disciplina, propina4 = Permission.objects.get_or_create(codename='delete_disciplinas', content_type=content_type_disciplina)

    """Permissão em notas"""
    add_nota, nota1 = Permission.objects.get_or_create(codename='add_notas', content_type=content_type_nota)
    change_nota, nota2 = Permission.objects.get_or_create(codename='change_notas', content_type=content_type_nota)
    view_nota, nota3 = Permission.objects.get_or_create(codename='view_notas', content_type=content_type_nota)
    delete_nota, nota4 = Permission.objects.get_or_create(codename='delete_notas', content_type=content_type_nota)

    """Permissões em propina"""
    add_propina, disciplina1 = Permission.objects.get_or_create(codename='add_propinas', content_type=content_type_propina)
    change_propina, disciplina2 = Permission.objects.get_or_create(codename='change_propinas', content_type=content_type_propina)
    view_propina, disciplina3 = Permission.objects.get_or_create(codename='view_propinas', content_type=content_type_propina)
    delete_propina, disciplina4 = Permission.objects.get_or_create(codename='delete_propinas', content_type=content_type_propina)

    """Permissões em movimentos"""
    add_movimento, movimento1 = Permission.objects.get_or_create(codename='add_movimentos', content_type=content_type_movimento)
    change_movimento, movimento2 = Permission.objects.get_or_create(codename='change_movimentos', content_type=content_type_movimento)
    view_movimento, movimento3 = Permission.objects.get_or_create(codename='view_movimentos', content_type=content_type_movimento)
    delete_movimento, movimento4 = Permission.objects.get_or_create(codename='delete_movimentos', content_type=content_type_movimento)

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