from flask import jsonify

from ...core import config
from ...main import app


@app.route(f"{config.API_V1_STR}/recognitions/", methods=["POST"])
def route_recognitions():
    return jsonify({'message': 'recognitions_entry_point'})
