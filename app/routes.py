from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def home() -> str:
    # TODO: implement database, not just mock data
    # create mock user data
    user = {"username": "Miguel"}
    # create mock post data
    posts = [
        {
            "author": {"username": "John"},
            "body": "Beautiful day in Portland!",
        },
        {
            "author": {"username": "Susan"},
            "body": "The Avengers movie was so cool!"
        },
    ]

    return render_template("index.html", title="Home", user=user, posts=posts)

