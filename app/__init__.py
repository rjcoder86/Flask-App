from flask import Flask
from .db import db
from .routes import main
from flask_swagger_ui import get_swaggerui_blueprint


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Ensure that the tables are created
    with app.app_context():
        db.create_all()

    app.register_blueprint(main, url_prefix='/api')  # Prefix for main routes
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app': "Flask Swagger Example"}
    )
    
    app.register_blueprint(swaggerui_blueprint, url_prefix='/api')  # Swagger UI at /api/swagger
    return app