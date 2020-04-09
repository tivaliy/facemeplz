import io
import uuid

from flask import render_template, request

from ..api import api
from ..main import app
from ..core import config
from ..storage import file_storage
from ..utils import timer
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
    elapsed_time = None
    if request.method == "POST":
        photo = request.files["file"]
        ext = f".{photo.content_type.split('/')[1]}"

        with timer() as t:
            bboxes = ssd_caffe_predictor.predict(photo)[0]
        elapsed_time = f"{t.elapsed:.2f}"
        # Set pointer at the very beginning after prediction phase
        photo.seek(0)

        # Draw bounding boxes for detected faces
        image = bb_draw(photo, bboxes, ext)

        public_url = file_storage.upload_file(
            io.BytesIO(image),
            f"photos/{uuid.uuid4().hex}{ext}",
            content_type=photo.content_type
        )

    return render_template(
        "index.html",
        url_path=public_url,
        bboxes=bboxes,
        elapsed_time=elapsed_time
    )
