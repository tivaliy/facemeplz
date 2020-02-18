import functools
from http import HTTPStatus

from flask import flash, jsonify, request, render_template

# Supported image types
IMAGE_MIME_TYPES = {
    'image/jpeg',
    'image/png'
}


def validate_request(original_function=None, *, template=None):
    """
    Request validator.

    :param original_function:
    :param template: Template file to be redirected to in case of errors.
                     Note: for validating API endpoints must be omitted.
    """
    def _decorate(f):

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            if request.method == "POST":
                file = request.files.get("file")

                if not file:
                    err_msg = "No file provided."
                    if template:
                        flash(err_msg)
                        return render_template(template)
                    return jsonify({'error': err_msg}), HTTPStatus.BAD_REQUEST

                mime_types = set(file.content_type.split(","))
                is_mime_type_allowed = any(
                    mime_types.intersection(IMAGE_MIME_TYPES))
                if not is_mime_type_allowed:
                    err_msg = "Not supported file format."
                    if template:
                        flash(err_msg)
                        return render_template(template)
                    return jsonify({"error": err_msg}), HTTPStatus.BAD_REQUEST

            return f(*args, **kwargs)
        return wrapper

    if original_function:
        return _decorate(original_function)

    return _decorate
