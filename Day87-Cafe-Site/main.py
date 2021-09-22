from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField


API_KEY = **********

app = Flask(__name__)
app.config['SECRET_KEY'] = **********
Bootstrap(app)

# create database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create TABLE config.
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


db.create_all()


class EditCafeForm(FlaskForm):
    name = StringField("Name of Cafe")
    map_url = StringField("Map URL")
    img_url = StringField("Image URL")
    location = StringField("Location")
    seats = StringField("No. of Seats")
    has_toilet = BooleanField("Has toilet?")
    has_wifi = BooleanField("Has wifi?")
    has_sockets = BooleanField("Has sockets?")
    can_take_calls = BooleanField("Can take calls?")
    coffee_price = StringField("Coffee Price")
    submit = SubmitField("Done")


class AddCafeForm(FlaskForm):
    name = StringField("Name of Cafe")
    map_url = StringField("Map URL")
    img_url = StringField("Image URL")
    location = StringField("Location")
    seats = StringField("No. of Seats")
    has_toilet = BooleanField("Has toilet?")
    has_wifi = BooleanField("Has wifi?")
    has_sockets = BooleanField("Has sockets?")
    can_take_calls = BooleanField("Can take calls?")
    coffee_price = StringField("Coffee Price")
    submit = SubmitField("Add Cafe")


@app.route("/")
def home():
    all_cafes = Cafe.query.all()
    return render_template("index.html", cafes=all_cafes)


@app.route("/update", methods=["POST", "GET"])
def update():
    form = EditCafeForm()
    cafe_id = request.args.get("id")
    cafe = Cafe.query.get(cafe_id)
    if form.validate_on_submit():
        cafe.rating = float(form.rating.data)
        cafe.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=cafe, form=form)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    cafe_id = request.args.get("id")
    cafe = Cafe.query.get(cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["POST", "GET"])
def add():
    form = AddCafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(name=form.name.data,
                        map_url=form.map_url.data,
                        img_url=form.img_url.data,
                        location=form.location.data,
                        seats=form.seats.data,
                        has_toilet=form.has_toilet.data,
                        has_wifi=form.has_wifi.data,
                        has_sockets=form.has_sockets.data,
                        can_take_calls=form.can_take_calls.data,
                        coffee_price=form.coffee_price.data)
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)

