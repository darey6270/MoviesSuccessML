from django.views.generic import TemplateView
from django.shortcuts import render, redirect
import joblib
from .forms import MoviesForm
import numpy as np


class AboutWebsite(TemplateView):
    template_name = "MoviesSuccess/about.html"


class ContactWebsite(TemplateView):
    template_name = "MoviesSuccess/contact.html"


class HomeWebsite(TemplateView):
    template_name = "MoviesSuccess/index.html"


def PredictionPage(request):
    prediction_text = ''
    predictForm = MoviesForm()
    if request.method == "POST":
        form = MoviesForm(request.POST)
        if True:
            year = request.POST['year']
            runtime = request.POST['runtime']
            rating = request.POST['rating']
            votes = request.POST['votes']
            revenue = request.POST['revenue']
            metascore = request.POST['metascore']
            action = request.POST['action']
            adventure = request.POST['adventure']
            animation = request.POST['animation']
            biography = request.POST['biography']
            comedy = request.POST['comedy']
            crime = request.POST['crime']
            drama = request.POST['drama']
            family = request.POST['family']
            fantasy = request.POST['fantasy']
            history = request.POST['history']
            horror = request.POST['horror']
            mystery = request.POST['mystery']
            scifi = request.POST['scifi']
            thriller = request.POST['thriller']

            model = joblib.load(open('MoviesSuccess/decisionTreeClassifier.pkl', 'rb'))
            pred_test = np.array(
                [year, runtime, rating, votes, revenue, metascore, action,
                 adventure, animation, biography, comedy, crime, drama,
                 family, fantasy, history, horror, 0, 0, mystery,
                 0, scifi, 0, thriller, 0, 0])
            result = model.predict(pred_test.reshape(1, -1))
            if result[0] == 1:
                prediction_text = "The movie is going to be a successfull one"
            else:
                prediction_text = "The movie might not be a successfull one"

            return render(request, "MoviesSuccess/result.html",
                          {"prediction_text": prediction_text})
        else:
            print(form.errors)
    else:
        predictForm = MoviesForm()
    return render(request, "MoviesSuccess/predict.html",
                  {"predictForm": predictForm})
