from flask import Flask, request

app = Flask(__name__)


@app.route("/ask", methods=["POST"])
def add_user():
    question = request.form['question']
    url = request.form['url']

    response = question + " for the image " + url

    return response


if __name__ == '__main__':
    app.run()
