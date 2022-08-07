from appone.models import DinosaurDB, DinosaurSelections
from appone import app
from flask import render_template, request, url_for, flash
from appone.dinosaurList import dinosaurs
from appone.recommender_code import get_recommendations


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', dinosaurs=dinosaurs)


def dinosaur():
    return "<h1>Dinosaur Page</h1>"


@app.route('/selectDinosaur', methods=['POST'])
def selectDinosaur():
    selectedDinosaur = request.form.get('dinosaur')
    result = get_recommendations(selectedDinosaur)
    return render_template('dinosaur.html', selectedDinosaur=selectedDinosaur, result=result, dinosaurs=dinosaurs)