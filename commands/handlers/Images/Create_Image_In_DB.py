from pathlib import Path
from models.imageModel import ImageModel
from models.SqlDB import db

def handle(UserEntryId,image):
    mainDir = Path(__file__).resolve().parents[2]
    imagesDir = mainDir / "images"
    imagesDir.mkdir(exist_ok=True)
    max_number = 0
    max_image = None
    for file in imagesDir.iterdir():
        name = file.name
        if name.startswith("image") and name.endswith(".png"):
            number_str = name[len("image"):-len(".png")] 
            if number_str.isdigit():
                number = int(number_str)
                if number > max_number:
                    max_number = number
                    max_image = file
    new_image_number = max_number + 1
    new_image_name = f"image{new_image_number}.png"
    new_image_path = imagesDir / new_image_name
    
    image.save(new_image_path)


    NewImageDb=ImageModel(entryId=UserEntryId,imagePath=str(new_image_path))
    db.session.add(NewImageDb)
    db.session.commit()
    return NewImageDb.to_dict()
