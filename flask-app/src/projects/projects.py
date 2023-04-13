from flask import Blueprint, request, jsonify, make_response
import json
from src import db


projects = Blueprint('projects', __name__)

# Get all projects from the DB
@projects.route('/projects', methods=['GET'])
def get_projects():
    cursor = db.get_db().cursor()
    cursor.execute('select * from Projects')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get project detail for project with particular project_id
@projects.route('/projects/<project_id>', methods=['GET'])
def get_project_detail(project_id):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Projects where project_id = {0}'.format(project_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

