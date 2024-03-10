from django.shortcuts import render, redirect

from ..forms import EstablishmentForm
from ..models import Establishment, EstablishmentQuestion, ClientResponse


def home(request):
    if request.method == 'POST':
        form = EstablishmentForm(request.POST)
        if form.is_valid():
            establishment = form.save()
            return redirect('questions', establishment_id=establishment.id)
    else:
        form = EstablishmentForm()
    return render(request, 'onboarding_forms/home.html', {'form': form})


def questions(request, establishment_id):
    establishment = Establishment.objects.get(id=establishment_id)
    questions = EstablishmentQuestion.objects.filter(establishment_type=establishment.establishment_type)
    if request.method == 'POST':
        for question in questions:
            response_text = request.POST.get(f'response{question.id}')
            response = ClientResponse(establishment=establishment, question=question, response_text=response_text)
            response.save()
        return redirect('success')
    return render(request, 'onboarding_forms/questions.html', {
        'establishment': establishment,
        'questions': questions
    })


def success(request):
    return render(request, 'onboarding_forms/success.html')


def establishments(request):
    establishments_list = Establishment.objects.all()
    return render(request, 'onboarding_forms/establishments.html', {
        'establishments': establishments_list,
    })
