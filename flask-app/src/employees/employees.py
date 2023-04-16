from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

employees = Blueprint('employees', __name__)

# Get all details about an employee with a specific employee_id
@employees.route('/employees/<employee_id>', methods=['GET'])
def get_employee_detail(employee_id):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Employees where employee_id = {0}'.format(employee_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get the name of the project(s) that an employee is working on
@employees.route('/employees/<employee_id>/projects', methods=['GET'])
def get_employee_project(employee_id):
    cursor = db.get_db().cursor()
    cursor.execute('select project_name from Projects p join Employees e on e.project_id = p.project_id where employee_id = {0}'.format(employee_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response