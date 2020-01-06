from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/main')
def mein():
    return "main"

from . import view
