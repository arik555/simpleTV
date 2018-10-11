from django import forms
from .models import Live, StarJalsha

class LiveForm(forms.ModelForm):

	class Meta:
		model = Live
		fields = '__all__'


class StarJalshaForm(forms.ModelForm):

	class Meta:
		model = StarJalsha
		fields = '__all__'

