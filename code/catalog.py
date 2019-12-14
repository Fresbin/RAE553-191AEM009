from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


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
    def post(self, name):
        if sel.find_by_name(name):
            return {'message': "An type with name '{}' already exists.".foramt(name)}

        data = Type.parser.parse_args()

        type = {'name': name, 'price': data['price']}

        try:
            Type.insert(type)
        except:
            return {"message": "An error occured inserting the type."}, 500

        return type, 201            
