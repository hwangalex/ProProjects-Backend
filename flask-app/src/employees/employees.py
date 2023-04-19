from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

employees = Blueprint('employees', __name__)

# Create a new employee
@employees.route('/employees', methods=['POST'])
def create_employee():
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
    
    query = 'insert into Employees (employee_id, first_name, last_name, country, city, state, zip_code, gender, date_of_birth, salary, project_id, is_remote, supervisor_id, team_id) values ('
    query += str(employee_id) + ', "'
    query += first_name + '", "'
    query += last_name + '", "'
    query += country + '", "'
    query += city + '", "'
    query += state + '", "'
    query += zip_code + '", "'
    query += gender + '", "'
    query += date_of_birth + '", "'
    query += salary + '", '
    query += str(project_id) + ', '
    query += str(is_remote) + ', '
    query += str(supervisor_id) + ', '
    query += str(team_id) + ')'

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return ("Success")

# Update a particular employee
@employees.route('/employees/<employee_id>/', methods=['PUT'])
def update_employee(employee_id):
    data = request.json
    
    first_name = data["updated_first_name"]
    last_name = data["updated_last_name"]
    country = data["updated_country"]
    city = data["updated_city"]
    state = data["updated_state"]
    zip_code = data["updated_zip_code"]
    gender = data["updated_gender"]
    date_of_birth = data["updated_date_of_birth"]
    salary = data["updated_salary"]
    project_id = data["updated_project_id"]
    is_remote = data["updated_is_remote"]
    supervisor_id = data["updated_supervisor_id"]
    team_id = data["updated_team_id"]

    query = 'update Employees set '
    query += 'first_name = "' + first_name + '", '
    query += 'last_name = "' + last_name + '", '
    query += 'country = "' + country + '", '
    query += 'city = "' + city + '", '
    query += 'state = "' + state + '", '
    query += 'zip_code = "' + zip_code + '", '
    query += 'gender = "' + gender + '", '
    query += 'date_of_birth = "' + date_of_birth + '", '
    query += 'salary = "' + salary + '", '
    query += 'project_id = ' + str(project_id) + ', '
    query += 'is_remote = ' + str(is_remote) + ', '
    query += 'supervisor_id = ' + str(supervisor_id) + ', '
    query += 'team_id = ' + str(team_id) + ' '
    query += 'where employee_id = ' + str(employee_id) + ' '

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return ("Success")

# Delete a particular employee
@employees.route('/employees/', methods=['DELETE'])
def employee():
    data = request.json
    employee_id = data["employee_id"]
    
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

# Get all employees (ID, fname, lname) in a specific team
@employees.route('/employees/team/<team_id>/', methods=['GET'])
def get_employees_on_team(team_id):
    cursor = db.get_db().cursor()
    cursor.execute('select employee_id, first_name, last_name from Employees where team_id = {0}'.format(team_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get information about a given employee's team
@employees.route('/employees/team_details/<employee_id>/', methods=['GET'])
def get_employee_team(employee_id):
    cursor = db.get_db().cursor()
    cursor.execute('select t.team_id, team_name, meeting_time, department_id from Teams t join Employees e on t.team_id = e.team_id where employee_id = {0}'.format(employee_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        row_dict = dict(zip(row_headers, row))
        meeting_time = row_dict.get('meeting_time')
        if meeting_time:
            # Extract the hours, minutes, and seconds from the timedelta object
            hours, remainder = divmod(meeting_time.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            # Format the time as a string in the format HH:MM:SS
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        row_dict['meeting_time'] = time_str
        json_data.append(row_dict)
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

# Get the name and ID of the project(s) that an employee is working on
@employees.route('/employees/<employee_id>/projects', methods=['GET'])
def get_employee_project(employee_id):
    cursor = db.get_db().cursor()
    cursor.execute('select project_name, project_id from Projects p join Employees e on e.project_id = p.project_id where employee_id = {0}'.format(employee_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

