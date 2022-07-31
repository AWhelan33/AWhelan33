from flask import Flask, render_template

app = Flask(__name__)

dinosaurs = [
    {
        'name': 'velociraptor',
        'diet': 'carnivorous',
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home')


def dinosaur():
    return "<h1>Dinosaur Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
