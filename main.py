from flask import Flask, render_template
import requests


app = Flask(__name__)
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_post = response.json()


@app.route('/')
def home():
    return render_template("index.html", all_post=all_post)


@app.route('/post/<int:num>')
def get_post(num):
    title = body = ""
    for post in all_post:
        if post["id"] == num:
            print(post["id"], num)
            title, body = post["title"], post["body"]
    return render_template("post.html", title=title, body=body)


if __name__ == "__main__":
    app.run(debug=True)
