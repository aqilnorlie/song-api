from flask import Blueprint, request
from extension import db
from models import Genre_song

genre_bp = Blueprint("genre_bp", __name__)

@genre_bp.route("/put/<genre_name>", methods=["POST"])
def put(genre_name):
    if request.method == "POST":
        genre_song = Genre_song(genre_name=genre_name)
        db.session.add(genre_song)
        db.session.commit()

        return {"status" : "success",
                "message" : "Genre created sucessfully !!"}

@genre_bp.route("/get", methods=["GET"])
@genre_bp.route("/get/<genre_name>", methods=["GET"])
def get(genre_name = None):
    if request.method == "GET":
        if genre_name is None:
            genre = Genre_song.query.all()
            all_genre = {}
            num = 0
            for data in genre:
                num += 1
                all_genre[f"Genre song {num}"] = {"id" : data.id, 
                "Genre name" : data.genre_name}
            return {"Status" : "success",
                    "Detail" : all_genre}
        else:
            genre_detail = Genre_song.query.filter_by(genre_name=genre_name).first()
            return {"status" : "success",
                "Id" : genre_detail.id,
                "Genre name" : genre_detail.genre_name}



