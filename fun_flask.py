from flask import Flask, request, make_response,jsonify
from flask_restful import Api, Resource, reqparse, fields, marshal
import config
# enviroment configurations
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'Naibor':
        return 'jojo'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'message':'unauthorized access'}),403)


if __name__ == '__main__':
    app.config.from_object(config.Development)
    app.run()