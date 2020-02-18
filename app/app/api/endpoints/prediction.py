from flask import jsonify, request

from ..validators import validate_request
from ...core import config
from ...main import app
from ...ml.predictor import ssd_caffe_predictor


@app.route(f"{config.API_V1_STR}/predictions/", methods=["POST"])
@validate_request
def route_predictions():
    bboxes = ssd_caffe_predictor.predict(request.files["file"])
    return jsonify({'boxes': bboxes})
