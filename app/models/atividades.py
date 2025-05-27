from config import db

class Atividade(db.Model):
    __tablename__ = 'atividades'

    atividade_id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, nullable=False)
    enunciado = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            'atividade_id': self.atividade_id,
            'professor_id': self.professor_id,
            'enunciado': self.enunciado
        }
    
    @staticmethod
    def criar_atividade(dados):
        campos = ["atividade_id", "professor_id", "enunciado"]

        for campo in campos:
            if campo not in dados:
                raise ValueError((f"Campo {campo} é obrigatório!"), 400)
        
        if Atividade.query.get(dados["atividade_id"]):
            raise ValueError(("atividade com esse ID já existe!"), 400)
        
        #Verificar professor

        enunciado = str(dados["enunciado"])

        nova_atividade = Atividade(
        atividade_id=dados['atividade_id'],
        professor_id=dados['professor_id'],
        enunciado=dados['enunciado']
        )

        db.session.add(nova_atividade)
        db.session.commit()
        
        return nova_atividade.serialize()
    
    @staticmethod
    def listar_atividades():
        return [atividade.serialize() for atividade in Atividade.query.all()]
    
    @staticmethod
    def obter_atividade(id):
        atividade = Atividade.query.get(id)
        return atividade.serialize() if atividade else None
    
    @staticmethod
    def atualizar_atividade(id, dados):
        atividade = Atividade.query.get(id)
        if not atividade:
            raise ValueError (("Atividade não encontrada!"), 404)
        
        ##Verificar professor

        if "enunciado" in dados:
            atividade.enunciado = dados["enunciado"]

        db.session.commit()
        return atividade.serialize()
    
    @staticmethod
    def deletar_atividade(id):
        atividade = Atividade.query.get(id)
        if not atividade:
            raise ValueError(("Atividade não encontrada!"), 404)
        db.session.delete(atividade)
        db.session.commit()