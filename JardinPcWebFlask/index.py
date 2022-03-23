from flask import Flask, render_template
from models import db, jardinPC

app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///database\\\jardinPC.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) #aca se hace la conexion con la db jardinPC

# Aca empiezan las rutas
@app.route('/')
def home ():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000)