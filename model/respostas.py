from config import db

class Respostas(db.Model):
    __tablename__ = 'notas'

    atividade_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
    aluno_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
    nota = db.Column(db.Float, nullable = True)
    resposta = db.Colum(db.String(50), nullable = False )

    def serealize(self):
        return{
            'aluno_id' : self.aluno_id,
            'nota' : self.nota,
            'resposta' : self.resposta
        }
    

    
