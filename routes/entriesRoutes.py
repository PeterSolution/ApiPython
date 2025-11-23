# ...existing code...
from flask import Blueprint, request, jsonify, abort
from flask_cors import CORS
import queries as query_dispatchers
import commands as command_dispatchers

entries_bp = Blueprint('entries_bp', __name__)
CORS(entries_bp, origins="http://localhost:3000", supports_credentials=True)

@entries_bp.route('/entries', methods=['GET'])
def get_entries():
    # pobieramy parametry paginacji z query string
    page = request.args.get('page', default=1, type=int)
    page_size = request.args.get('pagesize', default=20, type=int)

    result = query_dispatchers.dispatchers(
        'Get_entries_pagination',
        page,
        page_size
    )

    if not result:
        return jsonify([])

    return jsonify(result)


# def get_entry_by_id(entries_id=1, page_size=20):
#     result = query_dispatchers.dispatchers('Get_entries', entries_id,page_size)
# @entries_bp.route('/entries/<int:entries_id>', methods=['GET'])
# def get_entry_by_id(entries_id):
#     result = query_dispatchers.dispatchers('Get_entries', entries_id)
#     if not result:
#         abort(404)
#     return jsonify(result)


@entries_bp.route('/entries', methods=['POST'])
def add_entry():
    data = request.get_json()
    result = command_dispatchers.dispatchers('Create_entry', data)
    return jsonify(result), 200