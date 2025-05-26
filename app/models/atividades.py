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