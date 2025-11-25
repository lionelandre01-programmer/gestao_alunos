Sistema de Gestão de Alunos

Sistema desenvolvido para facilitar o gerenciamento de alunos em instituições de ensino. Permite o cadastro, listagem, edição, exclusão e acompanhamento de pagamentos de propinas, além de associar alunos a cursos e salas e muito mais.

📌 Funcionalidades

- Cadastro de alunos, cursos e salas  
- Gestão de mensalidades e pagamentos  
- Registro de propinas por mês (evitando duplicidade)  
- Relatórios de alunos por curso e sala  
- Sistema de autenticação 
- Interface web intuitiva

🛠 Tecnologias Usadas

- Backend: Python + Django  
- Frontend: HTML, CSS 
- Banco de Dados: SQLite3  
- Outros: JavaScript, Git/GitHub

📷 Capturas de Tela

> (Adicione imagens aqui se quiser mostrar o sistema funcionando)

🚀 Como Executar

1. Clone o repositório  
   git clone https://github.com/lione01-programmer/gestao_alunos.git

2. Instale as dependências  
   pip install -r requirements.txt

3. Aplique as migrações  
   python manage.py migrate

4. Inicie o servidor  
   python manage.py runserver

5. Acesse em:  
   http://127.0.0.1:8000/

📁 Organização

...
/alunos/
  models.py
  views.py
  forms.py
  urls.py
/templates/
  alunos/
    cadastro.html
    lista.html
...

👨🏽‍💻 Autor

Lionel Cristóvão André 
Estudante de Programação | Desenvolvedor Web
Site: https://lionelandre01-programmer.github.io/portfolio/
