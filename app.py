from flask import Flask
from flask_smorest import Api
from db import db
from resources.store import blp as StoreBlueprint
from resources.item import blp as ItemBlueprint

def create_app():
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
    api = Api(app)
    
    # Регистрация блюпринтов
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(ItemBlueprint)
    
    # Создание таблиц
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)