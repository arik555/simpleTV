from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404, HttpResponse
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .forms import UserLoginForm, UserRegisterForm, PasswordResetForm, ForgotPasswordForm

def login_user(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			form = UserLoginForm(request.POST or None)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				user = authenticate(username=username, password=password)
				login(request, user)
				messages.success(request, 'Login Success.')
				return redirect('home')
		else:
			form = UserLoginForm()
		context = {'form': form, 'title': 'Simple TV | Login', 'header': 'Login', 'login': 1}
		return render(request, 'accounts/commonformindex.html', context)
	else:
		return redirect('home')


def register_user(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			form = UserRegisterForm(request.POST or None)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.is_active = False
				instance.save()
				y = default_token_generator.make_token(instance)
				sts = custom_email(request, y+str(instance.id), instance.email, 0)
				# return HttpResponse(sts)
				messages.success(request, sts)
				return redirect('login_user')
		else:
			form = UserRegisterForm()
		context = {'form': form, 'title': 'Simple TV | Register', 'header': 'Register', 'register': 1}
		return render(request, 'accounts/commonformindex.html', context)
	else:
		return redirect('home')

def logout_user(request):
	if request.user.is_authenticated:
		logout(request)
		messages.success(request, 'Logout Success.')
		return redirect('home')
	else:
		return redirect('login_user')


def reset_password_universal(request, token=None):
	if token is None:
		if not request.user.is_authenticated:
			raise Http404
		if request.method == 'POST':
			form = PasswordResetForm(request.POST)
			if form.is_valid():
				user = User.objects.get(username=request.user)
				user.set_password(form.cleaned_data['password2'])
				user.save()
				logout(request)
				messages.success(request, 'Password Changed.')
				return redirect('home')
		else:
			form = PasswordResetForm()
		context = {'form': form, 'title': 'Simple TV | Password Reset', 'header': 'Change Password',}
		return render(request, 'accounts/commonformindex.html', context)
	if token is not None:
		user_id = int(token[-1])
		user_obj = User.objects.get(id=user_id)
		main_token = token[:-1]
		if default_token_generator.check_token(user_obj, main_token):
			if request.method == 'POST':
				form = PasswordResetForm(request.POST)
				if form.is_valid():
					user = User.objects.get(username=user_obj.username)
					user.set_password(form.cleaned_data['password2'])
					user.save()
					messages.success(request, 'Password Reset Done.')
					return redirect('login_user')
			else:
				form = PasswordResetForm()
			context = {'form': form, 'title': 'Simple TV | Password Reset', 'header': 'Reset Password',}
			return render(request, 'accounts/commonformindex.html', context)
		else:
			return HttpResponse('<h1>Invalid Token</h1>')

def forgot_password(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			form = ForgotPasswordForm(request.POST)
			if form.is_valid():
				user_email = form.cleaned_data['email']
				instance = User.objects.get(email=user_email)
				y = default_token_generator.make_token(instance)
				sts = custom_email(request, y+str(instance.id), instance.email, 1)
				messages.success(request, sts)
				return redirect('login_user')
		else:
			form = ForgotPasswordForm()
		context = {'form': form, 'title': 'Simple TV | Forgot Password', 'header': 'Verify', 'forgot': 1}
		return render(request, 'accounts/commonformindex.html', context)
	else:
		return redirect('login_user')

def custom_email(request, token=None, user_email=None, forgot=0):
	import datetime
	email_time = datetime.datetime.now()
	if token is not None and forgot == 0:
		subject = 'SimpleTV | Email Verification'
		from_email = str(settings.EMAIL_HOST_USER)
		to = [user_email,]
		myurl = request.get_host()+'/accounts/activate/'+token # account confirmation
		ctx = {
			'header': 'SimpleTV',
			'sub_header': 'Thank you for registering to our site. Please verify your email and activate your account.',
			'common_link': myurl,
			'verb': 'activate',
			'email_time': email_time,
		}
		message = get_template('accounts/emailindex.html').render(ctx)
		msg = EmailMessage(subject, message, to=to, from_email=from_email)
		# print(msg)
		msg.content_subtype = 'html'
		msg.send()
		status = 'Activation Link has been sent to your email address.'
		return status
		return HttpResponse('Activation Link has been sent to your email address.')
	elif token is not None and forgot == 1:
		subject = 'SimpleTV | Forgot Password'
		from_email = str(settings.EMAIL_HOST_USER)
		to = [user_email,]
		myurl = request.get_host()+'/accounts/reset/'+token # forgot_password
		ctx = {
			'header': 'SimpleTV',
			'sub_header': 'You have requested for a password reset. Please verify your account.',
			'common_link': myurl,
			'verb': 'verify & reset',
			'email_time': email_time,
		}
		message = get_template('accounts/emailindex.html').render(ctx)
		# print(type(message), message)
		msg = EmailMessage(subject, message, to=to, from_email=from_email)
		# print(msg)
		msg.content_subtype = 'html'
		msg.send()
		status = 'Verification Link has been sent to your email address.'
		return status

def account_confirmed(request, token=None):
	user_id = int(token[-1])
	user_obj = User.objects.get(id=user_id)
	main_token = token[:-1]
	if default_token_generator.check_token(user_obj, main_token):
		user_obj.is_active = True
		user_obj.save()
		messages.success(request, 'Your Account has been activated. You may login now.')
		return redirect('login_user')
	else:
		return HttpResponse('Accout was not activated.')
