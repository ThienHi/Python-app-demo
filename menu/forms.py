from django import forms
from .models import ListVideo


class ListVideoForm(forms.ModelForm):
    class Meta:
        model = ListVideo
        fields = ('url', 'image', 'content', 'creator')
