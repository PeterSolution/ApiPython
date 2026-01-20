from flask import Flask
from flask_cors import CORS
from models.SqlDB import db
from routes.userRoutes import user_bp
from routes.entriesRoutes import entries_bp
from routes.entriesInRowRoute import entersInRow_bp
from routes.ImagePatchRoute import image_bp
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
# app.config.from_pyfile('config.py')
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


CORS(app, resources={r"/*": {"origins": "http://aivision.local:11111"}}, supports_credentials=True)

db.init_app(app)  # powiązanie SQLAlchemy z aplikacją

# rejestracja blueprinta
app.register_blueprint(user_bp)
app.register_blueprint(entries_bp)
app.register_blueprint(entersInRow_bp)
app.register_blueprint(image_bp)

@app.route('/')
def index():
    return "Połączenie z SQL Server działa!"

if __name__ == '__main__':
    app.run(debug=True)