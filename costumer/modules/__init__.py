from flask import Blueprint

costumer_blueprint = Blueprint('costumers', __name__)

from . import resources
