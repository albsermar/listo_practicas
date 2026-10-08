from flask import Blueprint

notas_bp = Blueprint('notas', __name__)

@notas_bp.route('/notas')
def index():
    return "¡Hola desde la nueva feature de notas!"