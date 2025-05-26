from flask import Flask
from app.config.database import db
from app.routes.atividade_routes import atividade_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admin:SenhaForte123@host.docker.internal:3306/school-system"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(atividade_bp)

    with app.app_context():
        db.create_all()

    return app