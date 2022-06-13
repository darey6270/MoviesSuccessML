from django import forms


class MoviesForm(forms.Form):
    year = forms.DateField()
    runtime = forms.FloatField()
    rating = forms.FloatField()
    votes = forms.FloatField()
    revenue = forms.FloatField()
    metascore = forms.FloatField()
    action = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], required=True)
    adventure = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], required=True)
    animation = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], required=True)
    biography = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], required=True)
    comedy = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], required=True)
    crime = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], required=True)
    drama = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], required=True)
    family = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], required=True)
    fantasy = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], required=True)
    history = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], required=True)
    horror = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], required=True)
    music  = forms.FloatField()
    musical = forms.FloatField()
    mystery = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], required=True)
    romance = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], required=True)
    scifi= forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], required=True)
    sport = forms.FloatField()
    thriller = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], required=True)
    war = forms.FloatField()
    western = forms.FloatField()


