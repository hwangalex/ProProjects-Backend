from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

clients = Blueprint('clients', __name__)

# Get all details about a client with a specific client_id
@clients.route('/clients/<client_id>', methods=['GET'])
def get_client_detail(client_id):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Clients where client_id = {0}'.format(client_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

