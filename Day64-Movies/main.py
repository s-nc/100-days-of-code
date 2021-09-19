from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

API_KEY = ******

app = Flask(__name__)
app.config['SECRET_KEY'] = *******
Bootstrap(app)

# create database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# create entry
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(), nullable=True)
    img_url = db.Column(db.String(), nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Movie {self.title}>'


db.create_all()


class RateMovieForm(FlaskForm):
    rating = StringField("Your rating out of 10")
    review = StringField("Your Review")
    submit = SubmitField("Done")


class AddMovieForm(FlaskForm):
    title = StringField("Title of movie")
    # year = int(StringField("Year movie was made"))
    # description = StringField("Description of movie")
    # rating = float(StringField("Your rating out of 10"))
    # review = StringField("Your Review")
    # submit = SubmitField("Done")
    # img_url = StringField("Image URL")
    submit = SubmitField("Add Movie")

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")
# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    return render_template("index.html", movies=all_movies)


@app.route("/update", methods=["POST", "GET"])
def update():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete", methods=["GET"])
def delete():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["POST", "GET"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        parameters = {"api_key": API_KEY, "query": movie_title}
        response = requests.get(url="https://api.themoviedb.org/3/search/movie", params=parameters)
        data = response.json()["results"]
        print(data[0])
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)


@app.route("/get_data")
def get_movie_data():
    movie_id = request.args.get("id")
    if movie_id:
        movie_url = "https://api.themoviedb.org/3/movie/"+movie_id
        response = requests.get(url=movie_url, params={"api_key": API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            description=data["overview"],
            img_url="https://image.tmdb.org/t/p/w500/"+data["poster_path"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("update", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
