from flask_restful import Resource, Api

from costumer.modules import costumer_blueprint

consumer_restfull = Api(costumer_blueprint)


class CostumerResource(Resource):
    def get(self):
        return {'hello': 'costumers'}


consumer_restfull.add_resource(CostumerResource, '/')
