from flask import jsonify, request, Blueprint
from models.atividades import Atividade
from config import db

atividadesApp = Blueprint('atividades', __name__)

@atividadesApp.route('/atividades', methods=['POST'])
def post_atividade():
    dados = request.json
    try:
        nova_atividade = Atividade.criar_atividade(dados)
        return jsonify({"message": "Atividade criada com sucesso"}), 201
    except ValueError as e:
        return jsonify({"erro": str(e.args[0])}), e.args[1]
    

@atividadesApp.route('/atividades', methods=['GET'])
def listar_atividades():
    return jsonify(Atividade.listar_atividades()), 200

@atividadesApp.route('/atividades/<int:id>', methods=['GET'])
def obter_atividade(id):
    atividade = Atividade.obter_atividade(id)
    if not atividade:
        return jsonify({"erro": "Atividade não encontrado!"}), 404
    return jsonify(atividade), 200

@atividadesApp.route('/atividades/<int:id>', methods=['PUT'])
def atualizar_atividade(id):
    dados = request.json
    try:
        Atividade.atualizar_atividade(id, dados)
        return jsonify({"message": "Atividade atualizada com sucesso"}), 200
    except ValueError as e:
        return jsonify({"erro": str(e.args[0])}), e.args[1]

@atividadesApp.route('/atividades/<int:id>', methods=['DELETE'])
def deletar_atividade(id):
    try:
        Atividade.deletar_atividade(id)
        return jsonify({"mensagem": "Atividade deletada com sucesso!"}), 200
    except ValueError as e:
        return jsonify({"erro": str(e.args[0])}), e.args[1]
    
