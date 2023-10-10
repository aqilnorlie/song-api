from flask import Blueprint, request
from extension import db
from models import Category_song

category_bp = Blueprint("category_bp", __name__)

@category_bp.route("/put/<category_name>", methods=["POST"])
def put(category_name):
    if request.method == "POST":
        category_song = Category_song(type_song=category_name)
        db.session.add(category_song)
        db.session.commit()

        return {"status" : "success",
                "message" : "category song created sucessfully !!"}

@category_bp.route("/get", methods=["GET"])
@category_bp.route("/get/<category_name>", methods=["GET"])
def get(category_name = None):
    if request.method == "GET":
        if category_name is None:
            category = Category_song.query.all()
            all_category = {}
            num = 0
            for data in category:
                num += 1
                all_category[f"type song {num}"] = {"id" : data.id, 
                "Type Song" : data.type_song}
            return {"Status" : "success",
                    "Detail" : all_category}
        else:
            category = Category_song.query.filter_by(type_song=category_name).first()
            return {"status" : "success",
                "Id" : category.id,
                "Type song" : category.type_song}




