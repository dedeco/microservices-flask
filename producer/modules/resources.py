from flask_restful import Resource, Api

from producer.modules import producer_blueprint

producer_restfull = Api(producer_blueprint)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'producer'}


producer_restfull.add_resource(HelloWorld, '/')
