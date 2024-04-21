# Framework Django
- Django é um framework web Python de alto nível que incentiva o rápido desenvolvimento e um design limpo.
- O Django abstrai muito do trabalho do desenvolvedor, por cuidar de grande parte do desenvolvimento web, possibilitando o desenvolvedor focar apenas no core da sua aplicação.
- Para criar um projeto Django é necessário uma estrutura padrão que pode ser criada a partir do comando *django-admin startproject nome_do_projeto* na venv ou *python -m django startproject nome_do_projeto*.
- Para criar um app no Django é necessário uma estrutura padrão que pode ser criada a partir do comando *django-admin startapp nome_do_app* na venv ou *python -m django startapp nome_do_projeto*.
- Para iniciar o projeto: python manage.py *runserver*.


**Explicando a estrutura básica do Django:**
- *Manage:* 
    - É um wrapper em volta do django-admin.py.
    - Ele delega tarefas para o django-admin.py.
    - Responsável por colocar o pacote do projeto no sys.path.
    - Ele define a variável de ambiente DJANGO_SETTINGS_MODULE que aponta para o arquivo settings.py
    - Por isso, o manage.py é gerado automaticamente junto ao projeto, para facilitar o uso de comandos do django-admin.py (comandos administrativos).
- *WSGI:*
    - Web Service Gateway Interface - Interface de porta de entrada do servidor web.
    - Plataforma padrão para aplicações web em Python.
    - Serve de interface do Servidor Web e a Aplicação Web.
    - O Django com o comando startproject inicia uma configuração WSGI padrão para que se possa executar sua aplicação web.
    - Quando se inicia a aplicação Django com o comando runserver é iniciado um servidor de aplicação web leve. Esse servidor é especificado pela configuração WSGI_APPLICATION, lembrando que por padrão é configurado apenas um servidor para desenvolvimento, caso queira colocar a aplicação em produção é necessário configurar um servidor próprio.
- *SETTINGS:*
    - É o responsável pelas configurações do Django.
    - Nele é possível configurar por exemplo apps, conexão com banco de dados, template, time zone, cache, segurança, arquivos estáticos, etc.
- *URLS:*
    - É um schema URL.
    - Responsável por gerenciar as Rotas da URLs, onde é possível configurar pra onde cada rota será executada.
    - É uma forma limpa e elegante para gerenciar URLs.
- *VIEWS:*
    - Responsável por processar e retornar uma resposta para o cliente que fez a requisição.
- *MODELS:*
    - Define o modelo de dados inteiramente em Python.
    - Faz a abstração dos objetos de banco de dados para o Python, transformando todas as tabelas em classes e os acessos são feitos utilizando linguagem Python, onde o Django realiza a transformação para SQL.
- *ADMIN:*
    - Interface administrativa gerada automaticamente pelo Django.
    - Ele lê os metadados que estão nos models e fornece uma interface poderosa e pronta para manipulação de dados.
- *STATIC:*
    - Responsável por armazenar os arquivos estáticos.
    - CSS, JavaScript, imagens.
- *TEMPLATES:*
    - Responsável por armazenar os arquivos HTML.
    - O diretório templates é padrão para armazenar todo o conteúdo HTML da aplicação.

**Tabelas Padrões do Django:**
- O Django já possui tabelas padrões que são utilizadas principalmente para parte de segurança e autenticação.
- É possível criar as tabelas padrões do Django com o comando *migrate*.
- Ao criar as tabelas padrões do Django, é necessário criar um primeiro usuário para conseguir acessar o painel Django Administration.
- Para criar um primeiro usuário administrador é necessário o comando *createsuperuser*.
- As tabelas padrões consistem em auxiliar e agilizar toda parte de autenticação e também perfis de acesso.
- Entre as tabelas padrões estão as tabelas de Usuário, Grupo e de Perfil.
- Com as tabelas padrões, é possível criar usuários, grupos de usuários e definir perfis de qual usuário pode acessar determinado conteúdo.  
- Para criar as tabelas rode o comando *python manage.py migrate*.
- Para criar o admin *python manage.py createsuperuser --username admin*.
- No projeto criamos as tabelas em *models*.

**Migração de dados no Django:**
- Para migração de dados no Django, é necessário que tenha classes criadas.
- Com as classes criadas, para migração é utilizado o comando *migrate*.
- Pode ser utilizado o comando *migrations* para a criação de um arquivo de migração, sem a necessidade de migrar as "cegas".
- Pode ser utilizado o comando *sqlmigrate*, que ao invés de aplicar a migração, é gerado todo o comando para que essa migração possa ser efetuada manualmente no banco de dados.
- Criando um arquivo de migração *python manage.py makemigrations core(nome do app)* após isso é possível usar o comando *python manage.py sqlmigrate core 0001(nome da migration)*, para persistir a alteração é necessário rodar *python manage.py migrate core 0001*.
- Por fim registre o model em admin.py

**Templates:**
- O Django oferece no seu módelo de templates a capacidade de se utilizar expressões Python no HTML.
- Com isso é possível mostrar informações e realizar comandos IF e FOR.
- Para rederizar seu HTLM adicione-o nas *views*, crie uma rota para a sua requisição em *urls* e coloque a o diretório em *settings*.

**Pacote de autenticação do Django:**
- O Django já possui um pacote de autenticação que é empacotado em *django.contrib.auth*.
- Esse pacote cria as tabelas de usuários e permissões, onde fica mais fácil controlar as autenticações e permissões.
- Para se utilizar da autenticação padrão do Django é necessário que o pacote esteja entre os apps instalados no settings do projeto (essa configuração já vem pronta por default).
- *authenticate:*
    - A função authenticate do pacote *django.contrib.auth* é responsável por autenticar o usuário.
    - Importação: from django.contrib.auth import authenticate.
    - Utilização: user = authenticate(username=username, password=password).
- *login:*
    - A função login do pacote *django.contrib.auth* é responsável por criar uma sessão para o usuário autenticado.
    - Importação: from django.contrib.auth import login.
    - Utilização: login(request, user).
- *logout:*
    - A função logout do pacote *django.contrib.auth* é responsável por limpar os dados do usuário da sessão.
    - Importação: from django.contrib.auth import logout.
    - Utilização: user = logout(request).
- *login_required:*
    - A função login_required do pacote *django.contrib.auth.decorators* é responsável por autenticar o usuário.
    - Ela é um decorador que é utilizado em todas as funções/views que necessitam de um usuário logado/autenticado para serem acessadas.
    - Importação: from django.contrib.auth.decorators import login_required
    - Utilização: @login_required(login_url='/login/') acima da função/view.
- *decoradores:*
    - São funções que são usadas sobre outras funções.
    - Os decoradores são usados para extrair um código comum que deve ser aplicado para diversas funções.
    - A função login_required por exemplo, usada como decorador, faz com que seja realizada uma validação comum (usuário logado) para que em caso de usuário não logado, impeça a execução da função a qual ela está decorando.
