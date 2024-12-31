from flask import Blueprint, render_template

autor_routes = Blueprint('autor', __name__)

@autor_routes.route('/autor')
def autor():
    return render_template('autor/autor.html')
