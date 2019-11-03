from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return 'Hello World'

api.add_resource(Hello, '/hello') #http://127.0.0.1:5000/hello
app.run(port=5000)
