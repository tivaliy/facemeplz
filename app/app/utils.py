from io import BytesIO

from google.cloud import storage


def get_byte_fileobj(bucket, path):
    """
    Retrieve data from a given blob on Google Storage
    and pass it as a file object.

    :return: file object (BytesIO)
    """
    blob = _get_blob(bucket, path)
    byte_stream = BytesIO()
    blob.download_to_file(byte_stream)
    byte_stream.seek(0)
    return byte_stream


def get_bytestring(bucket, path):
    """
    Retrieve data from a given blob on Google Storage
    and pass it as a byte-string.

    :return: byte-string (needs to be decoded)
    """
    blob = _get_blob(bucket, path)
    return blob.download_as_string()


def upload_file(bucket, path, file_obj, content_type=None):
    """
    Upload file to Google Cloud Storage.

    :param bucket: Bucket name as a string.
    :param path: Path in a bucket of a file being uploaded.
    :param file_obj: A file handle open for reading.
    :param content_type: Optional type of content being uploaded.
    """
    blob = _get_blob(bucket, path)
    blob.upload_from_file(file_obj, content_type=content_type)
    return blob.public_url


def _get_blob(bucket_name, path):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(path)
    return blob
