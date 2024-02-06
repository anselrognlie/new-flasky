from flask import Blueprint, jsonify, make_response, abort
from ..db import db
from ..model.cat import Cat

bp = Blueprint("cats", __name__, url_prefix="/cats")

# You may see uses of Model.query to build queries.
# This is an older interface for queries that is considered legacy
# in SQLAlchemy. Prefer using db.session.execute(db.select(...)) instead.
# db.select resource: https://docs.sqlalchemy.org/en/20/tutorial/data_select.html

@bp.get("/")
def index():
    models = db.session.execute(db.select(Cat).order_by(Cat.id)).scalars()

    return list(map(Cat.to_dict, models))

@bp.get("/<id>")
def get(id):
    model = db.session.execute(db.select(Cat).filter_by(id=id)).scalar()
    if not model:
        abort(make_response(dict(detail=f"invalid id {id}"), 404))

    return model.to_dict()
