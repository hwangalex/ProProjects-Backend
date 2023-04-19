from flask import Blueprint, request, jsonify, make_response, current_app
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

# Create a new project
@projects.route('/projects', methods=['POST'])
def create_project():
    data = request.json
    
    client_id = data["client_id"]
    project_name = data["project_name"]
    project_difficulty = data["project_difficulty"]
    project_desc = data["project_desc"]
    
    query = 'insert into Projects (client_id, project_name, project_difficulty, project_desc) values ('
    query += str(client_id) + ', "'
    query += project_name + '", "'
    query += project_difficulty + '", "'
    query += project_desc + '")'

    
    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return ("Success")

# Update a particular project
@projects.route('/projects/<project_id>', methods=['PUT'])
def update_project(project_id):
    data = request.json
    
    client_id = data["updated_client_id"]
    project_name = data["updated_project_name"]
    project_difficulty = data["updated_project_difficulty"]
    project_desc = data["updated_project_desc"]
    
    query = 'update Projects set '
    query += str(project_id) + '",'
    query += str(client_id) + ', "'
    query += project_name + '", '
    query += project_difficulty + '",'
    query += project_desc + ')'

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return ("Success")

# Delete a particular project
@projects.route('/projects/', methods=['DELETE'])
def delete_project():
    data = request.json
    project_id = data["project_id"]
    
    query = 'delete from Projects where project_id = {0}'.format(project_id)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return ("Success")

# Get all tickets of a particular project_id
@projects.route('/projects/<project_id>/tickets', methods=['GET'])
def get_project_tickets(project_id):
    cursor = db.get_db().cursor()
    cursor.execute('select description, ticket_id, ticket_name, ticket_type_id from Tickets where project_id = {0}'.format(project_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all tickets of a particular project_id of a specific ticket type id
@projects.route('/projects/<project_id>/tickets/type/<ticket_type_id>', methods=['GET'])
def get_project_tickets_by_type(project_id, ticket_type_id):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Tickets where project_id = {0} and ticket_type_id = {1}'.format(project_id, ticket_type_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get detailed view of a particular ticket of a particular project
@projects.route('/projects/<project_id>/tickets/<ticket_id>', methods=['GET'])
def get_project_ticket_detail(project_id, ticket_id):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Tickets where project_id = {0} and ticket_id = {1}'.format(project_id, ticket_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Create a new ticket for a particular project
@projects.route('/projects/<project_id>/tickets/', methods=['POST'])
def create_project_ticket(project_id):
    data = request.json
    
    ticket_name = data["ticket_name"]
    ticket_type_id = data["ticket_type_id"]
    description = data["description"]
    
    query = 'insert into Tickets (ticket_name, ticket_type_id, description, project_id) values ("'
    query += ticket_name + '",'
    query += str(ticket_type_id) + ', "'
    query += description + '", '
    query += str(project_id) + ')'

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()


    return ("Success")

# Delete a particular ticket for a particular project
@projects.route('/projects/<project_id>/tickets/<ticket_id>', methods=['DELETE'])
def delete_project_ticket(project_id, ticket_id):
    
    query = 'delete from Tickets where ticket_id = {0}'.format(ticket_id)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return ("Success")

# Update a particular ticket of a particular project
@projects.route('/projects/<project_id>/tickets/<ticket_id>', methods=['PUT'])
def update_project_ticket(project_id, ticket_id):
    data = request.json
    
    ticket_name = data["ticket_name"]
    ticket_type_id = data["ticket_type_id"]
    description = data["description"]
    
    query = 'update Tickets set '
    query += 'ticket_name = "' + ticket_name + '", '
    query += 'ticket_type_id = ' + str(ticket_type_id) + ', '
    query += 'description = "' + description + '", '
    query += 'project_id = ' + str(project_id) + ' '
    query += 'where ticket_id = ' + str(ticket_id)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return ("Success")


# Get all employees working on a particular ticket of a particular project
@projects.route('/projects/<project_id>/tickets/<ticket_id>/employees', methods=['GET'])
def get_project_ticket_employees(project_id, ticket_id):
    cursor = db.get_db().cursor()
    # cursor.execute('select distinct Employees.employee_id, Employees.first_name, Tickets.ticket_id from Tickets join Ticket_Assignments join Employees where Tickets.ticket_id = {0}'.format(project_id, ticket_id))
    cursor.execute('select distinct e.employee_id, e.first_name, e.last_name, e.country, e.city, e.state, e.zip_code, e.gender, e.date_of_birth, e.salary, e.project_id, e.is_remote, e.supervisor_id, e.team_id from Ticket_Assignments join Employees e on Ticket_Assignments.employee_id = e.employee_id where Ticket_Assignments.ticket_id = 6'.format(project_id, ticket_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


