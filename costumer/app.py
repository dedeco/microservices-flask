import os

from costumer.modules import costumer_blueprint
from microservices import FlaskChassis

app = FlaskChassis(service_name="costumer", config_file="flask-dev.cfg").app
app.register_blueprint(costumer_blueprint, url_prefix='/api/v1/costumers')

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
