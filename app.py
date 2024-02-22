from flask import Flask, render_template, request

from sqlite import create_table, get_all_members, insert

app = Flask(__name__)

create_table()


@app.route("/")
def index():
    return render_template("form.html")


@app.route("/ranking")
def ranking():

    members = get_all_members()
    sorted_members = sorted(members, key=lambda x: x.score, reverse=True)

    return render_template("ranking.html", members=sorted_members)


@app.route("/submit", methods=["POST"])
def submit():

    name = request.json["username"]
    email = request.json["email"]
    score = request.json["randomScore"]

    insert(name, email, score)

    return {"message": "Member added"}, 201
