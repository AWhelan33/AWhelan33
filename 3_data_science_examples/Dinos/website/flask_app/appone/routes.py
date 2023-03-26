from appone.models import DinosaurDB, DinosaurSelections
from appone import app, db
from flask import render_template, request, url_for, flash, redirect
from appone.dinosaurList import dinosaurs
from appone.recommender_code import get_recommendations
from appone.models import DinosaurLiked, DinosaurSelections


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', dinosaurs=dinosaurs)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/attributes")
def attributes():
    return render_template('attributes.html')


@app.route('/selectDinosaur', methods=['POST'])
def selectDinosaur():
    selectedDinosaur = request.form.get('dinosaur')
    result = get_recommendations(selectedDinosaur)
    dino = DinosaurSelections(reccommendations=str(result))
    likedDino = DinosaurLiked(likedDinosaur=str(selectedDinosaur))
    db.session.add(dino, likedDino)
    db.session.commit()
    return render_template('dinosaur.html', selectedDinosaur=selectedDinosaur, result=result, dinosaurs=dinosaurs)


@app.route('/likedDinosaur', methods=['POST'])
def likedDinosaur():
    selectedDinosaur = request.form.get('dinosaur')
    likedDino = DinosaurLiked(likedDinosaur=str(selectedDinosaur))
    db.session.add(likedDino)
    db.session.commit()
    return render_template('thankYou.html', selectedDinosaur=selectedDinosaur)

@app.route('/support')
def support():
    return render_template('support.html')

