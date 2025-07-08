from flask import Blueprint, render_template, request, redirect, url_for
from app.models.db import mongo
from bson.objectid import ObjectId

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/')
def dashboard():
    interns = mongo.db.interns.find()
    return render_template('admin_dashboard.html', interns=interns)

@bp.route('/add', methods=['POST'])
def add_intern():
    name = request.form['name']
    team = request.form['team']
    task = request.form['task']
    mongo.db.interns.insert_one({'name': name, 'team': team, 'task': task})
    return redirect(url_for('admin.dashboard'))

@bp.route('/delete/<id>')
def delete_intern(id):
    mongo.db.interns.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('admin.dashboard'))
