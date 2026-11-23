from flask import Blueprint, send_from_directory
import os

images = Blueprint("assets", __name__, url_prefix="/assets")

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

@images.get("/<path:filename>")
def get_image(filename):
    return send_from_directory(ASSETS_DIR, filename)