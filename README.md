# mysite

Django Personal Blog

## 🛠️ Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas na sua máquina:

- [Python](https://www.python.org/) (versão 3.10 ou superior recomendada)
- `pip` (gerenciador de pacotes do Python)
- `git`

## ⚙️ Instalação e Configuração do Ambiente

Siga os passos abaixo para configurar o projeto localmente:

### 1. Clonar o repositório

```bash
git clone [https://github.com/Holandapt/mysite]
```

# É altamente recomendado o uso de um ambiente virtual para isolar as dependências do projeto.

exercute no terminal:

- python -m venv venv
- venv\Scripts\activate

# Instancie todas as bibliotecas necessárias:

- pip install -r requirements.txt

# Prepare as migrações do banco de dados:

- python manage.py migrate

# Para rodar o servidor de desenvolvimento localmente, execute:

- python manage.py runserver

# Para rodar a suíte de testes completa, execute:

- pytest
