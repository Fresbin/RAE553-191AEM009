from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

catalog_list={"type1":{"price":10},"type2":{"price":20},"type3":{"price":30}}

class Catalog(Resource):
    def get(self):
        return catalog_list
class Types(Resource):
    def get(self, type_name ):
        return catalog_list[type_name]
    def put(self, type_name):
        parser = reqparse.RequestParser()
        parser.add_argument("price")
        args = parser.parse_args()
        catalog_list[type_name]['price'] = args['price']
        return catalog_list[type_name]
    def delete(self, type_name):
        del catalog_list[type_name]
        return catalog_list
api.add_resource(Catalog, '/catalog_list') #http://127.0.0.1:5000/catalog_list
api.add_resource(Types, '/type/<type_name>') #http://127.0.0.1:5000/type_name
app.run(host='0.0.0.0',port=5000)
