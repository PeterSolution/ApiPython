from flask import Blueprint, request, jsonify, abort
from flask_cors import CORS
import queries as query_dispatchers
import commands as command_dispatchers

user_bp = Blueprint('user_bp', __name__)


# CORS(user_bp, origins="*", supports_credentials=False)

# CORS(user_bp, origins=[
#         "http://localhost:11111",
#         "http://192.168.56.1:11111",
#         "http://192.168.0.102:11111",
#         "http://172.21.80.1:11111",
#         "http://172.18.64.1:11111",
#         "http://172.17.32.1:11111",
#     ], supports_credentials=True)

#CORS(user_bp, origins="http://localhost:3000", supports_credentials=True)

@user_bp.route('/users', methods=['GET'])
def get_users():
    result = query_dispatchers.dispatchers('Get_all_users')
    return jsonify(result)

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    result = query_dispatchers.dispatchers('Get_user_by_id', user_id)
    if not result:
        abort(404)
    return jsonify(result)

@user_bp.route('/users/check', methods=['GET'])
def check_user():
    user_name = request.args.get('name')
    user_password = request.args.get('password')
    result = query_dispatchers.dispatchers('Check_user_exist', user_name, user_password)
    return jsonify(result)

@user_bp.route('/users/GetNamebyId/<string:user_name>', methods=['GET'])
def get_user_name_by_id(user_name):
    result = query_dispatchers.dispatchers('Get_user_id_by_name', user_name)
    return jsonify({
        "id": result
    })

@user_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    result = command_dispatchers.dispatchers('Create_user', data)
    return jsonify(result), 201

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    data = request.get_json()
    result = command_dispatchers.dispatchers('Update_user', user_id, data)
    return jsonify(result), 200

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    result = command_dispatchers.dispatchers('Delete_user', user_id)
    return jsonify(result), 200