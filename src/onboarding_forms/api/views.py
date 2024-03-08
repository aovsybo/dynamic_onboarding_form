from django.shortcuts import render, redirect
from ..forms import EstablishmentTypeForm, EstablishmentQuestionForm, EstablishmentForm
from ..models import Establishment, EstablishmentType


def index(request):
    if request.method == 'POST':
        establishment_type_form = EstablishmentTypeForm(request.POST)
        if establishment_type_form.is_valid():
            establishment_type = establishment_type_form.cleaned_data['establishment_type']
            establishment_form = EstablishmentForm()
            return render(request, 'onboarding_forms/details.html',
                          {'establishment_type': establishment_type, 'establishment_form': establishment_form})
    else:
        establishment_type_form = EstablishmentTypeForm()
    return render(request, 'onboarding_forms/index.html', {'establishment_type_form': establishment_type_form})


def save_establishment(request):
    if request.method == 'POST':
        establishment_type = request.POST.get('establishment_type')
        establishment_form = EstablishmentForm(request.POST)

        if establishment_form.is_valid():
            establishment = establishment_form.save(commit=False)
            establishment.establishment_type_id = establishment_type
            establishment.save()

            question_form = EstablishmentQuestionForm(establishment_type=establishment_type)
            return render(request, 'onboarding_forms/questions.html', {'question_form': question_form})
    return redirect('index')
