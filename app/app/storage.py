from abc import ABC, abstractmethod
from io import BytesIO

from google.cloud.storage import Client

from .core import config


class BaseFileStorage(ABC):
    """Base class to perform actions on files in a File Storage."""

    @abstractmethod
    def get_file(self, path: str) -> BytesIO:
        """
        Retrieve file from a File Storage.

        :param path: Path to file in a File Storage as a string
        """

    @abstractmethod
    def upload_file(self, file_obj: BytesIO, path: str, **kwargs):
        """
        Upload file to a File Storage.

        :param file_obj: File to be uploaded
        :param path: Path in File Storage where to upload a file
        """


class GCFileStorage(BaseFileStorage):
    """Class to perform actions on files in the Google Cloud Storage."""

    def __init__(self, bucket_name: str, client: Client = None) -> None:
        self._client = client or Client()
        self.bucket_name = bucket_name
        self._bucket = self._client.bucket(self.bucket_name)

    def get_file(self, path: str) -> BytesIO:
        return self._bucket.blob(path).download_as_string()

    def upload_file(self, file_obj: BytesIO, path: str, **kwargs) -> str:
        blob = self._bucket.blob(path)
        blob.upload_from_file(
            file_obj,
            content_type=kwargs.get('content_type')
        )
        return blob.public_url


file_storage = GCFileStorage(config.GCP_STORAGE_BUCKET_NAME)
