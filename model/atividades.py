from config import db

class Atividades(db.Model):
    __tablename__ = 'atividades'

    atividade_id = db.Column(db.Integer, primary_key = True)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    enunciado = db.Column(db.String(50), nullnable = False)


    professor = db.relationship('Professores', backref=db.backref('turmas', lazy=True))

    def serealize(self):
        return {
            'atividades_id' : self.atividades_id, 
            'professor_id': self.professor.serialize() if self.professor_id else None
        }