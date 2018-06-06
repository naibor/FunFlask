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


candidates = [{
    'id':1,
    'name':'John Doe',
    'describe':'from local  joint',
    'single':False
},
{
    'id':2,
    'name':'Jane Doe',
    'describe':'get a job first',
    'single':False
}
]

candidate_fields = {
    'name':fields.String,
    'describe':fields.String,
    'single':fields.Boolean,
    'uri':fields.Url('person')
    }
class UserApi(Resource):
    # define the arguments and how to validate it
    def __init__(self):
        pass
    def get(self):
        pass
    def put(self):
        pass
    def post(self):
        pass
    def delete(self):
        pass


class CandidatesApi(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type = str, required = True, 
        help = 'Give us a name', location = 'json')
        self.reqparse.add_argument('describe', type = str, required = True, location = 'json')
        super(CandidatesApi,self).__init__()
        
        
    def get(self):
        return {'candidates':[marshal(candidates, candidate_fields)]}

    def post(self):
        args = self.reqparse.parse_args()
        person  = {
            'id':candidates[-1]['id'] + 1,
            'name':args['name'],
            'describe':args['describe'],
            'single':False
        }
        candidates.append(person)
        return{'person':marshal(person, candidates_fields)},201 #created

    


# add_resource registers the route with the framework using given endpoints

# api.add_resource(UserApi, '/users/<int:id>', endpoint = 'user')

api.add_resource(CandidatesApi, '/fun/api/v1/candidates', endpoint= 'candidates')
# for the list of tasks
api.add_resource(PersonApi, '/fun/api/v1/person/<int:id>', endpoint='person')
# for a particular task
 
if __name__ == '__main__':
    app.config.from_object(config.Development)
    app.run()