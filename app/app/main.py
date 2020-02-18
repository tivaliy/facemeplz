from flask import Flask, render_template

app = Flask(__name__)

# Setup app
from .core import app_setup  # noqa


def register_error_handlers(app_inst):
    def render_error(exc):
        return render_template(f"errors/{exc.code}.html", error=exc), exc.code

    for e in (401, 404, 500):
        app_inst.errorhandler(e)(render_error)


register_error_handlers(app)


if __name__ == "__main__":
    # Only for debugging while developing
    # register error handlers
    app.run(host='0.0.0.0', debug=True, port=80)
