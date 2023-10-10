from extension import db

class Category_song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_song = db.Column(db.String(100), nullable=False)
    song_detail = db.relationship('Song_detail', backref='category_song')

class Genre_song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(100), nullable=False)
    song_detail = db.relationship('Song_detail', backref='genre_song')

class Song_detail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(100), nullable=False)
    singer_name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category_song.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre_song.id'))



