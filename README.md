Markdown
# 📇 API de Geração de Nomes Aleatórios

Uma API REST simples, rápida e moderna para gerar nomes e apelidos fictícios, ideal para alimentar bases de dados de testes, popular interfaces gráficas ou testar sistemas com dados realistas.

Construída com **Python**, **FastAPI** e **Faker**, pronta a correr localmente ou em contentores **Docker**.

---

## 🚀 Funcionalidades

* Geração de nomes e apelidos realistas (configurado por defeito para português de Portugal `pt_PT`).
* Quantidade configurável de resultados por pedido (1 a 1000).
* Documentação interativa automática (Swagger UI).
* Pronta para produção com Docker.

---

## 🛠️ Tecnologias Utilizadas

* [Python 3.12+](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/) - Framework web de alta performance.
* [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI rápido.
* [Faker](https://faker.readthedocs.io/) - Biblioteca de geração de dados falsos.
* [Docker](https://www.docker.com/) - Para isolamento e encapsulamento da aplicação.

---

## 📦 Estrutura do Projeto

```text
.
├── main.py             # Código principal da API e rotas
├── requirements.txt    # Dependências do Python
├── Dockerfile          # Instruções para construir a imagem Docker
├── .dockerignore       # Ficheiros a ignorar pelo Docker
└── README.md           # Documentação do projeto
```

💻 Como Instalar e Executar (Localmente)
Pré-requisitos
Python 3.12 ou superior instalado na máquina.

Passos
Clonar o repositório:

```Bash
git clone [https://github.com/o-teu-utilizador/nome-do-repositorio.git](https://github.com/o-teu-utilizador/nome-do-repositorio.git)
cd nome-do-repositorio
```

Criar um ambiente virtual (Recomendado):

```Bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

Instalar as dependências:

```Bash
pip install -r requirements.txt
```

Iniciar o servidor:

```Bash
uvicorn main:app --reload
```

A API estará disponível em http://127.0.0.1:8000.

🐳 Como Instalar e Executar (com Docker)
Se preferires não instalar o Python localmente, podes correr a API de forma totalmente isolada com o Docker.

Pré-requisitos
Docker instalado e a correr na máquina.

Passos
Construir a imagem da aplicação:

```Bash
docker build -t gerador-nomes-api .
```

Executar o contentor:

```Bash
docker run -d -p 8000:8000 --name api-nomes gerador-nomes-api
```

A API estará disponível na mesma porta local: http://127.0.0.1:8000.

📖 Como Usar a API
Endpoints Disponíveis
1. Testar o estado da API
URL: /

Método: GET

Resposta: Confirma que a API está a correr.

2. Gerar Nomes
URL: /api/nomes

Método: GET

Parâmetros de Query:

quantidade (Opcional, Inteiro): O número de nomes a gerar. O valor por defeito é 10. (Máximo: 1000).

Exemplo de Pedido:

```Plaintext
GET [http://127.0.0.1:8000/api/nomes?quantidade=3](http://127.0.0.1:8000/api/nomes?quantidade=3)
```

Exemplo de Resposta:

```JSON
{
  "dados": [
    {
      "nome": "João",
      "apelido": "Silva"
    },
    {
      "nome": "Maria",
      "apelido": "Santos"
    },
    {
      "nome": "Carlos",
      "apelido": "Ferreira"
    }
  ]
}
```

🕹️ Documentação Interativa
Graças ao FastAPI, tens acesso automático a uma interface Swagger onde podes testar os endpoints diretamente no teu browser.

Para acederes, com o servidor a correr, visita:
👉 http://127.0.0.1:8000/docs

🤝 Contribuir
Sente-te à vontade para fazer um fork do projeto e enviar Pull Requests. Para grandes mudanças, por favor abre uma Issue primeiro para discutirmos o que gostarias de alterar.
