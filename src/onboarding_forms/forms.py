from django import forms
from .models import EstablishmentType, EstablishmentQuestion, Establishment


class EstablishmentTypeForm(forms.Form):
    establishment_type = forms.ModelChoiceField(queryset=EstablishmentType.objects.all(), empty_label=None)


class EstablishmentQuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        establishment_type = kwargs.pop('establishment_type')
        super(EstablishmentQuestionForm, self).__init__(*args, **kwargs)

        questions = EstablishmentQuestion.objects.filter(establishment_type=establishment_type)

        for question in questions:
            self.fields[f'question_{question.id}'] = forms.CharField(label=question.question_text)


class EstablishmentForm(forms.ModelForm):
    class Meta:
        model = Establishment
        fields = ['title', 'city', 'address', 'is_new']