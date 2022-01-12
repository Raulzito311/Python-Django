from django.forms import ModelForm, fields, models
from .models import (
    Questionario
)

class QuestionarioForm(ModelForm):
    class Meta:
        model = Questionario
        fields = '__all__'