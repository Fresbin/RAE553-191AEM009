from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


catalog_list={"type1":{"price":10},"type2":{"price":20},"type3":{"price":30}}

class Catalog(Resource):
    @jwt_required()
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM types"
        result = cursor.execute(query)
        row = cursor.fetchall()
        catalog_list = {}
        for type in row:
            catalog_list[type[0]] = {"name":type[0], "price":type[1]}
        return catalog_list
class Types(Resource):
    TABLE_NAME = 'types'

    parser = reqparse.RequestParser()
    parser.add_argument('price',
         type=float,
         required=True,
         help="This field cannot be left blank!"
    )

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
        if self.find_by_name(type_name):
            return {'message': "An type with name '{}' already exists.".format(type_name)}

        data = Types.parser.parse_args()

        type = {'name': type_name, 'price': data['price']}

        try:
            Types.insert(type)
        except:
            return {"message": "An error occured inserting the type."}, 500

        return type, 201
    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM types WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'type': {'name': row[0], 'price': row[1]}}

    @classmethod
    def insert (cls, type):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO types VALUES (?, ?)"
        cursor.execute(query, (type['name'], type['price']),)

        connection.commit()
        connection.close()

    @jwt_required()
    def delete(self, type_name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM types WHERE name=?"
        cursor.execute(query, (type_name,))

        connection.commit()
        connection.close()

        return {'message': 'Type deleted'}

    @jwt_required()
    def put(self, type_name):
        data = Types.parser.parse_args()
        type = self.find_by_name(type_name)
        updated_type_name = {'name': type_name, 'price': data['price']}
        if type is None:
            try:
                Types.insert(updated_type_name)
            except:
                raise
                return {"message": "An error occured updating the type."}
        return updated_type_name

    @classmethod
    def update(cls, type):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor('data')
        cursor = connection.cursor()

        query = "UPDATE types WHERE name=? SET price=?"
        cursor.execute(query, (type['name'], type['price']),)

        connection.commit()
        connection.close()
