from flask import Blueprint, jsonify
from fish_data import FISH

api = Blueprint("api", __name__, url_prefix="/api")

# -----------------------
# HEALTH API ENDPOINT
# -----------------------

@api.route("health")
def health():
    return jsonify({"status":"ok"}), 200

# ----------------
# FISH ROUTES
# ---------------

@api.route("fish")
def get_fish():
    return jsonify(FISH)


