from .models import  CountriesList, Answers
from django.forms import ModelForm, TextInput, Textarea


class CountryQuiz(ModelForm):
    class Meta:
        model = Answers
        fields = ["answer"]
        widgets = {"answer": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название столицы',
                                              'autocomplete': 'off'})}
