from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_request
def cria_banco():
    app.before_request_funcs[None].remove(cria_banco)
    db.create_all()
    
api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

# Verificando o nome do módulo
if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)