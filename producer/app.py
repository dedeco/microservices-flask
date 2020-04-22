import os

from microservices import FlaskChassis
from producer.modules import producer_blueprint

app = FlaskChassis(service_name="producer", config_file="flask-dev.cfg").app
app.register_blueprint(producer_blueprint, url_prefix='/api/v1/producers')

port = int(os.environ.get('PORT', 8081))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
