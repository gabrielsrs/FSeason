from flask import Blueprint

from controllers.search_controller import search_controller
from controllers.game_controller import game_controller

handle = Blueprint("handle", __name__)


@handle.route("/", methods=["POST", "GET"])
def fseason():
    return search_controller()


@handle.route("/<game>/<region>/<name>")
def home(game, region, name):
    return game_controller(game, region, name)
