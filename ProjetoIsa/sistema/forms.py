from django.forms import ModelForm, fields, models
from .models import (
    Questionario,
    Pessoa,
    Localizacao
)

class QuestionarioForm(ModelForm):
    class Meta:
        model = Questionario
        fields = '__all__'


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class LocalizacaoForm(ModelForm):
    class Meta:
        model = Localizacao
        fields = '__all__'