from flask import Blueprint, request, jsonify, abort
from flask_cors import CORS
import queries as query_dispatchers
import commands as command_dispatchers
from pathlib import Path

image_bp = Blueprint('image_bp', __name__)
CORS(image_bp, origins=[
        "http://localhost:11111",
        "http://192.168.56.1:11111",
        "http://192.168.0.102:11111",
        "http://172.21.80.1:11111",
        "http://172.18.64.1:11111",
        "http://172.17.32.1:11111",
    ], supports_credentials=True)

@image_bp.route('/images/<int:entry_id>', methods=['GET'])
def get_images_by_entry_id(entry_id):
    result = query_dispatchers.dispatchers('Get_images_by_entry_id', entry_id)
    if not result:
        abort(404)
    return result, 200

@image_bp.route('/images', methods=['POST'])
def add_image():
    UserEntryId = request.form.get('entryId')
    image = request.files.get('image')
    if UserEntryId is None or image is None:
        abort(400, description="entryId and image are required")
    result = command_dispatchers.dispatchers('Create_Image_In_DB', UserEntryId, image)
    if not result:
        abort(500, description="server error")
    return jsonify(result), 200
    # patch = "C:\\ImagesAi"
    # try:
    #     open("place.txt","x")
    #     with open("place.txt","a") as file:
    #         file.write("Ksiegowość")
    # except:
    #     pass
    # self.place=open("place.txt","r").readline()
    
    
    
    # mainDir = Path(__file__).resolve().parent.parent
    # imagesDir = mainDir / "images"
    # imagesDir.mkdir(exist_ok=True)
    # max_number = 0
    # max_image = None
    # for file in imagesDir.iterdir():
    #     name = file.name
    #     if name.startswith("image") and name.endswith(".png"):
    #         number_str = name[len("image"):-len(".png")]  # SUBSTRING
    #         if number_str.isdigit():
    #             number = int(number_str)
    #             if number > max_number:
    #                 max_number = number
    #                 max_image = file
    # new_image_number = max_number + 1
    # new_image_name = f"image{new_image_number}.png"

    # print(f"Main directory: {mainDir}")

# add_image()