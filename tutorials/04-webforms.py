from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "<NEED_TO_INPUT>"

# import os
# os.urandom(24).hex()


messages = [
    {"title": "Message One", "content": "Message One Content"},
    {"title": "Message Two", "content": "Message Two Content"},
]


@app.route("/")
def index():
    return render_template("forms_index.html", messages=messages)


@app.route("/create/", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if not title:
            flash("Title is required!")
        elif not content:
            flash("Content is required!")
        else:
            messages.append({"title": title, "content": content})
            return redirect(url_for("index"))

    return render_template("forms_create.html")
