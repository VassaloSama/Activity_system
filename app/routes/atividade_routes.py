from flask import Blueprint
from app.controllers import atividade_controller

atividade_bp = Blueprint('atividade_bp', __name__)

atividade_bp.route('/atividades', methods=['GET'])(atividade_controller.listar_atividades)
atividade_bp.route('/atividades/<int:atividade_id>', methods=['GET'])(atividade_controller.obter_atividade)
atividade_bp.route('/atividades', methods=['POST'])(atividade_controller.criar_atividade)
atividade_bp.route('/atividades/<int:atividade_id>', methods=['PUT'])(atividade_controller.atualizar_atividade)
atividade_bp.route('/atividades/<int:atividade_id>', methods=['DELETE'])(atividade_controller.deletar_atividade)
