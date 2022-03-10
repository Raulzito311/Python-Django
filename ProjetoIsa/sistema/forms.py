from django.forms import ModelForm, MultipleChoiceField, fields, models
from .models import (
    Questionario,
    Pessoa
)

class QuestionarioForm(ModelForm):
    class Meta:
        model = Questionario
        fields = '__all__'


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'