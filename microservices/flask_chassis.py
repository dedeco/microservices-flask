import os

from flask import Flask

from .health_checks import health_check


class FlaskChassis(object):
    """
     Pattern: Microservice chassis just with externalized configuration and health check
    """

    config_finalised: bool = False
    _db = None
    _app = None
    _service_name = None
    _config_file = None

    def __init__(self, app: Flask = None, service_name: str = None, config_file: str = None, ):
        """
        :param app: A flask application
        :param service_name: Microservice name
        """
        self._app = app
        self._service_name = service_name
        self._config_file = config_file

        if not app:
            self._app = Flask(__name__, instance_relative_config=True)

        self.init_app()

    def init_app(self):
        """Initialises extension on app
        """

        self.load_external_config()

        # Set default configuration
        self._add_blueprints()

        if not hasattr(self.app, 'extensions'):
            self._app.extensions = {}
        self._app.extensions['flask-chassis'] = self

    def _add_blueprints(self):
        """
        Adds common blueprints to app
        """
        self._app.register_blueprint(health_check, url_prefix='/health')

    def load_external_config(self):
        """
        Loads external config file if path supplied by environmental variable.
        Call this after loading config in microservice to give precendence to
        file at 'EXT_CONFIG_PATH'.
        """
        if self._config_file is not None:
            self._app.config.from_pyfile(self._config_file, silent=False)
        else:
            self._app.config.from_pyfile(os.environ.get('EXT_CONFIG_PATH'), silent=False)
            self._app.config["SERVICE_NAME"] = self.service_name
        self.config_finalised = True

    @property
    def db(self):
        if self._db is None:
            from flask_sqlalchemy import SQLAlchemy
            self._db = SQLAlchemy(self.app)
        return self._db

    @property
    def app(self):
        return self._app

    @property
    def service_name(self):
        return self._service_name or "name x"
