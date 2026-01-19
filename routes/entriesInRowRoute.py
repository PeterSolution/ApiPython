from flask import Blueprint, request, jsonify, abort
from flask_cors import CORS
import queries as query_dispatchers
import commands as command_dispatchers

entersInRow_bp = Blueprint('entersInRow_bp', __name__)
CORS(entersInRow_bp,origins=[
        "http://localhost:11111",
        "http://192.168.56.1:11111",
        "http://192.168.0.102:11111",
        "http://172.21.80.1:11111",
        "http://172.18.64.1:11111",
        "http://172.17.32.1:11111",
    ],supports_credentials=True)

@entersInRow_bp.route('/entriesInRow/<int:user_id>',methods=['GET'])

def get_entries_in_row(user_id):
    result = query_dispatchers.dispatchers('GetEntriesInRow', user_id)
    if not result:
        abort(404)
    return jsonify(result), 200
@entersInRow_bp.route('/entriesInRow', methods=['POST'])
def add_entry_in_row():
    data = request.get_json()
    userid= data.get('userId')
    if(userid is None):
        abort(400, description="userId is required")
    result = command_dispatchers.dispatchers('Create_entry_in_row', userid)
    return jsonify(result), 200
@entersInRow_bp.route('/entriesInRow/<int:user_id>', methods=['PUT'])
def update_entry_in_row(user_id):
    result = command_dispatchers.dispatchers('Update_entry_in_row', user_id)
    return jsonify(result), 200