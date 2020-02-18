from predictme import CaffeObjectDetector

from ..core import config
from ..utils import get_byte_fileobj


prototxt = get_byte_fileobj(
    config.GCP_STORAGE_BUCKET_NAME,
    config.CAFFE_SSD_PROTOTXT_CONFIG_PATH
).getvalue()

model_weights = get_byte_fileobj(
    config.GCP_STORAGE_BUCKET_NAME,
    config.CAFFE_SSD_MODEL_WEIGHT_CONFIG_PATH
).getvalue()

# This instance mast be shared across project
ssd_caffe_predictor = CaffeObjectDetector(prototxt, model_weights)
