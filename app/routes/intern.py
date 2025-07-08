from flask import Blueprint, render_template
from app.models.db import mongo

bp = Blueprint('intern', __name__, url_prefix='/intern')

@bp.route('/<name>')
def intern_dashboard(name):
    intern = mongo.db.interns.find_one({'name': name})
    return render_template('intern_dashboard.html', intern=intern)
