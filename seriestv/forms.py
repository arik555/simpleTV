from django import forms
from .models import Series, Episode

class SeriesForm(forms.ModelForm):

	class Meta:
		model = Series
		fields = '__all__'


class EpisodeForm(forms.ModelForm):

	class Meta:
		model = Episode
		fields = '__all__'

