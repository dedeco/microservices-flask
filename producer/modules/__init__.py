from flask import Blueprint

producer_blueprint = Blueprint('producers', __name__)

from . import resources