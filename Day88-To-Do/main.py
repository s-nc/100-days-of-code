# My To-Do List.

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


API_KEY = *****

app = Flask(__name__)
app.config['SECRET_KEY'] = *****
Bootstrap(app)

# create database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tasks.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create TABLE config.
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False)


db.create_all()


class AddTaskForm(FlaskForm):
    description = StringField(label="")
    submit = SubmitField("Add")


@app.route("/", methods=["GET", "POST"])
def home():
    all_tasks = Task.query.order_by(Task.completed).all()
    form = AddTaskForm()
    if form.validate_on_submit():
        new_task = Task(description=form.description.data,
                        completed=False)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("index.html", form=form, tasks=all_tasks)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    task_id = request.args.get("id")
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/update", methods=["GET", "POST"])
def update():
    task_id = request.args.get("id")
    task = Task.query.get(task_id)
    print(task.completed)
    task.completed = not task.completed
    print(task.completed)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

