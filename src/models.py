from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80))
    password = db.Column(db.String(120))

    def __repr__(self):
        return '<Users %r>' % self.email

    def serialize(self):
        return{
            "email": self.email,
            "password": self.password
        }


class Quizes(db.Model):
    __tablename__ = 'quizes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return '<Quiz %r>' % self.quiz

    def serialize(self):
        return {
            "quiz" : self.quiz
        }


class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizes.id'))
    question = db.Column(db.String(160))
    a = db.Column(db.String(120))
    b = db.Column(db.String(120))
    c = db.Column(db.String(120))
    d = db.Column(db.String(120))

    def __repr__(self):
        return '<Question %r>' % self.question

    def serialize(self):
        return {
            "id" : self.id,
            "question" : self.question, 
            "options":{
                "a" : self.a,
                "b" : self.b,
                "c" : self.c,
                "d" : self.d
            }
        }

