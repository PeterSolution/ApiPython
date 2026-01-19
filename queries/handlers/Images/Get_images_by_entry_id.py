from flask import send_file
from models.imageModel import ImageModel

def handle(entry_id: int):
    images = ImageModel.query.filter_by(entryId=entry_id).first()
    if not images:
        return None
    
    # return [image.to_dict() for image in images]

    imageToSend = send_file(images.imagePath, mimetype='image/png')
    return imageToSend