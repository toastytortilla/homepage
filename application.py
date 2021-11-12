import time
import random
from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Configure CS50 Library to use SQlite database
db = SQL("sqlite:///visitors.db")

COMMENTS = [
    "Wow, great website!",
    "Yeah, I think tortillas are pretty great, too.",
    "I like what you've done with the place.",
    "Next time we hang out, I'll buy the drinks!",
    "Can you make ME a website?!",
    "hey.",
    "Wanna grab some tacos sometime?",
    "Can you tell me more about Bootstrap?",
    "Let's hang out sometime!",
    "Love the color palette :D",
    "The color palette is very 90's Taco Bell 🔥",
    "Sweet site, brahh",
    "My dog loves your website.",
    "This site feels homey, nice work!"
]

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":
        # Generate random int for assigning visitor comments
        i = random.randint(0,(len(COMMENTS) - 1))

        # Validate submission
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        comment = COMMENTS[i]

        # Remember visitor
        db.execute("INSERT INTO visitors (first_name, last_name, comment) VALUES (?, ?, ?)", first_name, last_name, comment)

        # Reload page
        time.sleep(1)
        return redirect("/contact")

    else:
        # Display page
        visitors = db.execute("SELECT first_name, comment FROM visitors ORDER BY visitor_id DESC")
        return render_template("contact.html", visitors=visitors)
