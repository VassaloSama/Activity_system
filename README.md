# API Atividades

API desenvolvida com Flask e SQLAlchemy para gerenciamento de atividades, seguindo o padrão MVC. Ideal para instituições que desejam controlar a geração de atividades por professores e notas de alunos.

## 🛠️ Tecnologias

- Python 3
- Flask
- SQLAlchemy
- MySQL
- Flasgger (Swagger UI)

## 📁 Estrutura

```
app/
├── app.py # Ponto de entrada da aplicação Flask
├── config.py # Configurações de ambiente e banco de dados
├── models/
| └── atividade.py # Model de Atividade
├── controller/
│ └── atividades.py # Controller de Atividades
```

## ⚙️ Configuração

### API School-System
Necessário da API School-System para funcionamento disponível em https://github.com/VassaloSama/School-System

### Banco de Dados

A aplicação utiliza MySQL. O arquivo `config.py` já possui um exemplo de conexão via `pymysql`:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:SenhaForte123@host.docker.internal:3306/school-system"
```
⚠️ Altere as credenciais e host conforme seu ambiente.

## 🔌 Endpoints
### ATIVIDADES
GET /atividades - Lista todas as atividades.

GET /atividades/<span style="color:blue">{id}</span> - Retorna os dados de uma atividade.

POST /atividades - Cria uma nova atividade.

PUT /atividades/<span style="color:blue">{id}</span> - Atualiza os dados de uma atividade

DELETE /atividades/<span style="color:blue">{id}</span> - Deleta uma atividade

### RESETAR
POST /atividades/resetar
Reseta atividades no banco


📌 Observações
Swagger UI está disponível em /apidocs (habilitado por padrão com Flasgger).


# 🛜 Integrações
#### API School-System
repositório: https://github.com/VassaloSama/School-System

#### API Reservation-System
repositório: https://github.com/GabrielCecconi25/Reservation-System