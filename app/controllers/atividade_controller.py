from flask import jsonify, request, abort
from app.models.atividade import Atividade
from app.config.database import db
import requests


def verificar_professor(professor_id):
    url = f"http://localhost:5000/professores/{professor_id}"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        abort(404, description="Professor não encontrado no sistema de gerenciamento escolar.")


def listar_atividades():
    atividades = Atividade.query.all()
    return jsonify([atividade.serialize() for atividade in atividades]), 200


def obter_atividade(atividade_id):
    atividade = Atividade.query.get(atividade_id)
    if not atividade:
        abort(404, description="Atividade não encontrada")
    return jsonify(atividade.serialize()), 200


def criar_atividade():
    dados = request.get_json()

    if not all(campo in dados for campo in ['atividade_id', 'professor_id', 'enunciado']):
        abort(400, description="Campos obrigatórios: atividade_id, professor_id, enunciado")

    if Atividade.query.get(dados['atividade_id']):
        abort(400, description="Atividade com esse ID já existe!")

    verificar_professor(dados['professor_id'])

    nova_atividade = Atividade(
        atividade_id=dados['atividade_id'],
        professor_id=dados['professor_id'],
        enunciado=dados['enunciado']
    )

    db.session.add(nova_atividade)
    db.session.commit()

    return jsonify(nova_atividade.serialize()), 201


def atualizar_atividade(atividade_id):
    dados = request.get_json()

    atividade = Atividade.query.get(atividade_id)
    if not atividade:
        abort(404, description="Atividade não encontrada")

    if 'professor_id' in dados:
        verificar_professor(dados['professor_id'])
        atividade.professor_id = dados['professor_id']

    atividade.enunciado = dados.get('enunciado', atividade.enunciado)

    db.session.commit()

    return jsonify(atividade.serialize()), 200


def deletar_atividade(atividade_id):
    atividade = Atividade.query.get(atividade_id)
    if not atividade:
        abort(404, description="Atividade não encontrada")

    db.session.delete(atividade)
    db.session.commit()

    return jsonify({'mensagem': 'Atividade deletada com sucesso'}), 200
