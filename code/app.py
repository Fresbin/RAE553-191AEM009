from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
app = Flask(__name__)
app.secret_key = 'toms@77'
api = Api(app)
jwt = JWT(app, authenticate, identity)
catalog_list={"type1":{"price":10},"type2":{"price":20},"type3":{"price":30}}

class Catalog(Resource):
    @jwt_required()
    def get(self):
        return catalog_list
class Types(Resource):
    @jwt_required()
    def get(self, type_name ):
        return catalog_list[type_name]
    def put(self, type_name):
        if type_name not in catalog_list:
            catalog_list[type_name] = {"price": ""}
        parser = reqparse.RequestParser()
        parser.add_argument("price")
        args = parser.parse_args()
        catalog_list[type_name]['price'] = args['price']
        return catalog_list[type_name]
    def delete(self, type_name):
        del catalog_list[type_name]
        return catalog_list
    def post(self, type_name):
        if type_name in catalog_list:
            parser = reqparse.RequestParser()
            parser.add_argument("price")
            args = parser.parse_args()
            catalog_list[type_name]['price'] = args['price']
            return catalog_list[type_name]
        else:
            return "Error {} type is not in catalog list".format(type_name)
api.add_resource(Catalog, '/catalog_list') #http://127.0.0.1:5000/catalog_list
api.add_resource(Types, '/type/<type_name>') #http://127.0.0.1:5000/type_name
app.run(host='0.0.0.0',port=5000)