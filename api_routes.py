from flask import Blueprint, jsonify
from fish_data import FISH, ALL_FISH

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
    return jsonify(FISH), 200

@api.route("fish/<int:fish_id>")
def get_fish_by_id(fish_id):
    fish = next((f for f in ALL_FISH if f["id"] == fish_id), None)
    if fish is None:
        return jsonify({"error": "Fish not found"}), 404
    return jsonify(fish), 200