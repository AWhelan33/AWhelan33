from flask import Flask, render_template

app = Flask(__name__)

dinosaurs = [
    {
        'name': 'velociraptor',
        'diet': 'carnivorous',
        'imageName': 'static/velociraptor.png'
    },
    {
        'name': 'aardonyx',
        'diet': 'herbivorous',
        'imageName': 'static/aardonyx.jpeg'
    },
    {
        'name': 'abelisaurus',
        'diet': 'herbivorous',
        'imageName': 'static/abelisaurus.jpeg'
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', dinosaurs=dinosaurs)


def dinosaur():
    return "<h1>Dinosaur Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
