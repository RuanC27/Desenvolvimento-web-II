from flask import Blueprint, render_template, request
from models.Problema import Problema

problema_routes = Blueprint('problema', __name__)

@problema_routes.route('/problema', methods=['GET'])
def enunciado():
    return render_template('problema/enunciado.html')

@problema_routes.route('/resultado', methods=['POST'])
def resultado():
    variavel1 = request.form.get('variavel1')
    variavel2 = request.form.get('variavel2')
    problema = Problema(variavel1, variavel2)
    resultado = problema.calcular()
    return render_template('problema/resultado.html', resultado=resultado)
