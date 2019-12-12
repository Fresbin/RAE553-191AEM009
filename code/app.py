from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from user import UserRegister
from catalog import Catalog , catalog_list, Types


app = Flask(__name__)
app.secret_key = 'toms@77'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Catalog, '/catalog_list') #http://127.0.0.1:5000/catalog_list
api.add_resource(Types, '/type/<type_name>') #http://127.0.0.1:5000/type_name
api.add_resource(UserRegister, '/register') #http://127.0.0.1:5000/register

app.run(host='0.0.0.0',port=5000)
