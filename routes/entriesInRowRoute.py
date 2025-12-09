from flask import Blueprint, request, jsonify, abort
from flask_cors import CORS
import queries as query_dispatchers
import commands as command_dispatchers

entersInRow_bp = Blueprint('entersInRow_bp', __name__)
CORS(entersInRow_bp,origins="http://aivision.local:10623",supports_credentials=True)

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
    data = request.get_json()
    result = command_dispatchers.dispatchers('Update_entry_in_row', user_id, data)
    return jsonify(result), 200