from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from main import main as main_blueprint

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['DEBUG']=True
    
    app.register_blueprint(main_blueprint)
    
    db.init_app(app)

    @app.route('/')
    def index():
        names=['david','sadrim','tania']
        return render_template('iniciativa.html', names=names)

    @app.route('/', methods=['POST'])
    def send():
        return render_template('iniciativa.html')

    return app


