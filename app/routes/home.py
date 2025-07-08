from flask import Blueprint, render_template
from app.models.db import mongo

bp = Blueprint('home', __name__)

@bp.route('/')
def home():
    interns = mongo.db.interns.find()
    return render_template('home.html', interns=interns)
