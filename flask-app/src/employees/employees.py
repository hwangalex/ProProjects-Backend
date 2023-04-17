from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

employees = Blueprint('employees', __name__)

# Create a new employee
@employees.route('/employees/<employee_id>/', methods=['POST'])
def create_employee(employee_id):
    data = request.json
    
    employee_id = data["employee_id"]
    first_name = data["first_name"]
    last_name = data["last_name"]
    country = data["country"]
    city = data["city"]
    state = data["state"]
    zip_code = data["zip_code"]
    gender = data["gender"]
    date_of_birth = data["date_of_birth"]
    salary = data["salary"]
    project_id = data["project_id"]
    is_remote = data["is_remote"]
    supervisor_id = data["supervisor_id"]
    team_id = data["team_id"]
    
    query = 'insert into Employees (employee_id, first_name, last_name, country, city, state, zip_code, gender, date_of_birth, salary, project_id, is_remote, supervisor_id, team_id) values ("'
    query += str(employee_id) + '",'
    query += first_name + ', "'
    query += last_name + '", '
    query += country + '",'
    query += state + '",'
    query += zip_code + ', "'
    query += gender + '", '
    query += str(date_of_birth) + '",'
    query += salary + '",'
    query += str(project_id) + ', "'
    query += str(is_remote) + '", '
    query += str(supervisor_id) + '",'
    query += str(team_id) + ')'

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return ("Success")

# Update a particular employee
@employees.route('/employees/<employee_id>/', methods=['PUT'])
def update_employee(employee_id):
    data = request.json
    
    employee_id = data["employee_id"]
    first_name = data["first_name"]
    last_name = data["last_name"]
    country = data["country"]
    city = data["city"]
    state = data["state"]
    zip_code = data["zip_code"]
    gender = data["gender"]
    date_of_birth = data["date_of_birth"]
    salary = data["salary"]
    project_id = data["project_id"]
    is_remote = data["is_remote"]
    supervisor_id = data["supervisor_id"]
    team_id = data["team_id"]

    query = 'update Employees set '
    query += str(employee_id) + '",'
    query += first_name + ', "'
    query += last_name + '", '
    query += country + '",'
    query += state + '",'
    query += zip_code + ', "'
    query += gender + '", '
    query += str(date_of_birth) + '",'
    query += salary + '",'
    query += str(project_id) + ', "'
    query += str(is_remote) + '", '
    query += str(supervisor_id) + '",'
    query += str(team_id) + ')'

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return ("Success")

# Delete a particular employee
@employees.route('/employees/<employees_id>/', methods=['DELETE'])
def employee(employee_id):
    
    query = 'delete from Employees where employee_id = {0}'.format(employee_id)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return ("Success")

# Get all details about an employee with a specific employee_id
@employees.route('/employees/<employee_id>/', methods=['GET'])
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

# Get all employees
@employees.route('/employees/', methods=['GET'])
def get_all_employees():
    cursor = db.get_db().cursor()
    cursor.execute('select * from Employees')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all employees (ID) in a specific team
@employees.route('/employees/team/<team_id>/', methods=['GET'])
def get_employees_on_team(team_id):
    cursor = db.get_db().cursor()
    cursor.execute('select employee_id from Employees where team_id = {0}'.format(team_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all employees (ID) that are remote
@employees.route('/employees/is_remote/', methods=['GET'])
def get_employee_remote():
    cursor = db.get_db().cursor()
    cursor.execute('select employee_id from Employees where is_remote = True')
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

