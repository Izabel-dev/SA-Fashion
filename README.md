# Fashion Modas - Projeto Django

Este projeto é uma loja de roupas funcional desenvolvida em Django, com sistema de autenticação (login e cadastro), páginas protegidas para gerenciamento de produtos, categorias e pedidos, além de uma API RESTful.

## Funcionalidades

- **Autenticação de Usuários**: Cadastro e Login de usuários.
- **Páginas Protegidas**: Acesso restrito a funcionalidades de gerenciamento apenas para usuários autenticados.
- **Gerenciamento de Produtos (CRUD)**: Adicionar, Visualizar, Editar e Excluir produtos.
- **Gerenciamento de Categorias (CRUD)**: Adicionar, Visualizar, Editar e Excluir categorias de produtos.
- **Gerenciamento de Pedidos (CRUD)**: Adicionar, Visualizar, Editar e Excluir pedidos.
- **API RESTful**: Endpoints para acesso e manipulação de dados via API.
- **Mensagens de Feedback**: Notificações para o usuário sobre o sucesso ou falha das operações.
- **Interface Web Responsiva**: Utiliza Bootstrap para uma experiência de usuário consistente.

## Requisitos

- Python 3.8+
- pip (gerenciador de pacotes do Python)

## Instalação e Configuração

Siga os passos abaixo para configurar e rodar o projeto localmente:

1.  **Clone o repositório (se aplicável) ou navegue até a pasta do projeto:**

    ```bash
    cd /home/
    ```

2.  **Instale as dependências do Python:**

    ```bash
    sudo pip3 install django djangorestframework django-cors-headers
    ```

3.  **Execute as migrações do banco de dados:**

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

4.  **Crie um superusuário (administrador):**

    ```bash
    python3 manage.py createsuperuser
    ```
    Siga as instruções no terminal para criar seu usuário e senha.

5.  **Inicie o servidor de desenvolvimento:**

    ```bash
    python3 manage.py runserver 0.0.0.0:8000
    ```

## Acessando a Aplicação

Após iniciar o servidor, você pode acessar a aplicação nos seguintes endereços:

-   **Página Inicial**: `http://localhost:8000/home/`
-   **Login**: `http://localhost:8000/login/`
-   **Cadastro**: `http://localhost:8000/register/`
-   **Admin**: `http://localhost:8000/admin/` (Use o superusuário criado)
-   **API Root**: `http://localhost:8000/api/`

## Rotas da API

-   `/api/categorias/`
-   `/api/produtos/`
-   `/api/pedidos/`
-   `/api/clientes/`

Você pode interagir com a API usando ferramentas como Postman, Insomnia ou diretamente pelo navegador (para métodos GET).

## Estrutura do Projeto

```
. # Raiz do projeto
├── core/ # Projeto Django principal
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py # Configurações do projeto
│   ├── urls.py # URLs principais do projeto
│   └── wsgi.py
├── loja/ # Aplicação Django 'loja'
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py # Configurações do admin
│   ├── apps.py
│   ├── models.py # Definição dos modelos de dados
│   ├── views.py # Lógica das views web
│   ├── api_views.py # Lógica das views da API
│   ├── forms.py # Definição dos formulários
│   ├── serializers.py # Serializadores para a API
│   └── urls.py # URLs da aplicação 'loja'
├── templates/ # Modelos HTML
│   ├── base.html # Template base com Bootstrap e navegação
│   ├── loja/ # Templates específicos da aplicação 'loja'
│   │   ├── home.html
│   │   ├── categoria_list.html
│   │   ├── categoria_form.html
│   │   ├── produto_list.html
│   │   ├── produto_form.html
│   │   ├── pedido_list.html
│   │   ├── pedido_form.html
│   │   └── confirm_delete.html
│   └── registration/ # Templates de autenticação
│       ├── login.html
│       └── register.html
├── static/ # Arquivos estáticos (CSS, JS, imagens)
│   ├── css/
│   └── js/
├── manage.py # Utilitário de linha de comando do Django
└── README.md # Este arquivo
```
