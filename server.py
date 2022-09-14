from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home_page():
    year = datetime.now().year
    random_number = randint(1, 9)
    return render_template("practice_index.html", num=random_number, year=year)


@app.route('/guess/<guessed_name>')
def get_details(guessed_name):
    parameters = {
        "name": guessed_name
    }
    gender_response = requests.get("https://api.genderize.io", params=parameters)
    age_response = requests.get("https://api.agify.io", params=parameters)
    gender = gender_response.json()["gender"]
    age = age_response.json()["age"]
    return render_template("guess.html", name=guessed_name, gender=gender, age=age)


@app.route('/blog/<num>')
def blog_data(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    data = response.json()
    return render_template("blog.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
