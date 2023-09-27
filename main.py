from flask import Flask
import random

app = Flask(__name__)

number = random.randint(0, 9)

@app.route("/")
def guess():
    return "<b>Guess a number between 0 and 9</b> <br> <img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif " \
           "width=200 height=200>"

@app.route("/<int:guess_number>")
def guess_number(guess_number):
    global number
    if number > guess_number:
        return "<b>Guess higher please</b> <br> <img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif " \
           "width=200 height=200>"
    elif number < guess_number:
        return "<b>Guess lower please</b> <br> <img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif " \
               "width=200 height=200>"
    else:
        return "<b>Yes!</b> <br> <img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif " \
               "width=200 height=200>"

if __name__ == "__main__":
    app.run(debug=True)