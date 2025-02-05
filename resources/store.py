from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import StoreModel
from schemas import StoreSchema

blp = Blueprint("stores", __name__, description="Операции с магазинами")

@blp.route("/store/<int:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        try:
            db.session.delete(store)
            db.session.commit()
            return {"message": "Магазин удален"}
        except SQLAlchemyError:
            abort(500, message="Произошла ошибка при удалении магазина")

    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def put(self, store_data, store_id):
        store = StoreModel.query.get_or_404(store_id)
        try:
            store.name = store_data["name"]
            store.description = store_data.get("description")
            db.session.commit()
        except IntegrityError:
            abort(400, message="Магазин с таким именем уже существует")
        except SQLAlchemyError:
            abort(500, message="Ошибка при обновлении магазина")
        return store

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Магазин с таким именем уже существует")
        except SQLAlchemyError:
            abort(500, message="Ошибка при создании магазина")
        return store