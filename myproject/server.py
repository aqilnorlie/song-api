from __init__ import create_app
from blueprint.category_song import category_bp
from blueprint.genre_song import genre_bp


app = create_app()
app.register_blueprint(category_bp, url_prefix="/category")
app.register_blueprint(genre_bp, url_prefix="/genre")

@app.route("/")
def hello():
    return "<h1>Hello this is song API!</h1>"

if __name__ == "__main__":
    app.run(debug=True)

