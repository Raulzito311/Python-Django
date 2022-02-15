from django.forms import ModelForm, MultipleChoiceField, fields, models
from .models import (
    Questionario,
    Pessoa,
    Localizacao
)

class QuestionarioForm(ModelForm):
    CHOICES =(
        ("PR", "Proprietário"),
        ("PO", "Posseiro"),
        ("AS", "Assentado"),
        ("AR", "Arrendatário"),
        ("PA", "Parceiro"),
        ("US", "Usufruário"),
    )
    #titulos = MultipleChoiceField(choices = CHOICES)
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