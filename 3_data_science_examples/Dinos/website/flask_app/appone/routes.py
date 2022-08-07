from appone.models import DinosaurDB, DinosaurSelections
from appone import app, db
from flask import render_template, request, url_for, flash
from appone.dinosaurList import dinosaurs
from appone.recommender_code import get_recommendations
from appone.models import DinosaurLiked, DinosaurSelections


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
    dino = DinosaurSelections(reccommendations=str(result))
    db.session.add(dino)
    db.session.commit()
    return render_template('dinosaur.html', selectedDinosaur=selectedDinosaur, result=result, dinosaurs=dinosaurs)


@app.route('/likedDinosaur', methods=['POST'])
def likedDinosaur():
    likedDinosaur = request.form.get('dinosaur')
    dino = DinosaurLiked(likedDinosaur=str(likedDinosaur))
    db.session.add(dino)
    db.session.commit()
    return render_template('thankYou.html')
