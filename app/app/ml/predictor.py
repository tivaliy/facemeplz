from predictme import CaffeObjectDetector

from ..core import config
from ..storage import file_storage


# TODO: Add some kind of a 'caching' layer to store instances of predictors
#  that are configured for different batch size of images, since there is
#  some weird behaviour when we try to change batch size 'on fly'.

# Fetch SSD-related config data that is stored in Google Cloud Storage
prototxt = file_storage.get_file(config.CAFFE_SSD_PROTOTXT_CONFIG_PATH)
weights = file_storage.get_file(config.CAFFE_SSD_MODEL_WEIGHT_CONFIG_PATH)

# This instance must be shared across project
ssd_caffe_predictor = CaffeObjectDetector(prototxt, weights)
