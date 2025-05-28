from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

app = Flask(__name__) 
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 5002
app.config['DEBUG'] = True

# Configuração do Swagger
app.config['SWAGGER'] = {
    'title': 'API Atividades',
    'uiversion': 3
}
swagger = Swagger(app)

# Config Banco MySQL
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:SenhaForte123@host.docker.internal:3306/school-system"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)