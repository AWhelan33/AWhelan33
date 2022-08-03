from flask import Flask, render_template
from dinosaurList import dinosaurs
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', dinosaurs=dinosaurs)


def dinosaur():
    return "<h1>Dinosaur Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
