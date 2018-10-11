from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django import forms

class UserLoginForm(forms.Form):
	username = forms.CharField(max_length=10)
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				return self.cleaned_data
			else:
				raise forms.ValidationError('Please activate your account to login.')
		else:
			raise forms.ValidationError('Username or Password Incorrect.')

class UserRegisterForm(forms.ModelForm):
	password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password')

	def clean(self):
		x = False
		p1 = self.cleaned_data['password']
		p2 = self.cleaned_data['password2']
		email = self.cleaned_data['email']
		user_name = self.cleaned_data['username']
		user_count1 = User.objects.filter(email=email).count()
		user_count2 = User.objects.filter(username=user_name).count()
		if user_count1 > 0:
			raise forms.ValidationError('Email already exists.')
		elif user_count2 > 0:
			raise forms.ValidationError('User already exists.')
		elif p1 != p2:
			raise forms.ValidationError('Passwords Mismatch.')
		else:
			return self.cleaned_data

class PasswordResetForm(forms.Form):
	password1 = forms.CharField(widget=forms.PasswordInput, label='New Password')
	password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

	def clean(self):
		p1 = self.cleaned_data['password1']
		p2 = self.cleaned_data['password2']

		if p1 != p2:
			raise forms.ValidationError('Passwords Mismatch.')
		else:
			return self.cleaned_data

class ForgotPasswordForm(forms.Form):
	email = forms.EmailField(max_length=100)
