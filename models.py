from flask_sqlalchemy  import SQLAlchemy 


db= SQLAlchemy()

class JardinPC(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    cod= db.Column(db.Integer)
    image= db.Column(db.String(200), unique=True, nulleable=False) #aca va la imagen en lugar del string
    name= db.Column(db.String(200), unique=True, nulleable=False)
    price = db.Column(db.Real)
    description = db.Column(db.String(200), unique=True, nulleable=False)
    