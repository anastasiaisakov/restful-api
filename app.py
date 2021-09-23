from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db
from resources.item import Item, ItemList
from security import authenticate, identity
from resources.user import UserRegister
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #it can be anything
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "jose"
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>') # instead of the decorator
api.add_resource(ItemList, '/items') # instead of the decorator
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__': # so it doesn't run when importing app
    db.init_app(app)
    app.run(port=5000, debug=True)
