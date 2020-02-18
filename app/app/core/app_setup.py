import io
import uuid

from flask import render_template, request

from ..api import api
from ..main import app
from ..core import config
from ..utils import upload_file
from ..ml.predictor import ssd_caffe_predictor
from ..ml.utils import bb_draw


app.config["SECRET_KEY"] = config.SECRET_KEY


@app.route("/", methods=["POST", "GET"])
@api.validate_request(template="index.html")
def index():
    """
    Index page.
    """

    public_url = None
    bboxes = None
    if request.method == "POST":
        photo = request.files["file"]
        ext = f".{photo.content_type.split('/')[1]}"

        bboxes = ssd_caffe_predictor.predict(photo)
        photo.seek(0)

        image = bb_draw(photo, bboxes, ext)

        public_url = upload_file(
            config.GCP_STORAGE_BUCKET_NAME,
            f"photos/{uuid.uuid4().hex}{ext}",
            io.BytesIO(image),
            content_type=photo.content_type
        )

    return render_template("index.html", filepath=public_url, bboxes=bboxes)
