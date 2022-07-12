from django.forms import ModelForm
from . import models


class DiaryForm(ModelForm):
    class Meta:
        model = models.Diary
        fields = ["user", "title", "paragraph"]