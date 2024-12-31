from flask import Blueprint, render_template

static_routes = Blueprint('static', __name__)

@static_routes.route('/')
def index():
    return render_template('index/index.html')
