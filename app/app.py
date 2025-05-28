from flask import jsonify
from config import app, db

from controller.atividade import atividadesApp

# Registrar Rota
app.register_blueprint(atividadesApp)

# Criar tabelas no banco
with app.app_context():
    db.create_all()

#### ROTA RESETAR DADOS ####
@app.route('/atividades/resetar', methods=['POST'])
def resetar_dados():
    from models.atividades import Atividade
    Atividade.query.delete()
    db.session.commit()

    return jsonify({"mensagem": "Dados resetados com sucesso!"}), 200
    
# Rodar o servidor
if __name__ == '__main__':
    app.run(
        host = app.config["HOST"],
        port = app.config['PORT'],
        debug = app.config['DEBUG']
        )