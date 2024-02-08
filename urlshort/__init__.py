from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = '09dfsjl45ngf9-4593458235jlkjfs'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app