from django.urls import path
from .views import (
	login_user, register_user, logout_user, forgot_password, account_confirmed, reset_password_universal
	)

urlpatterns = [
	path('reset/<slug:token>', reset_password_universal, name='reset_password_universal'),
	path('reset/', reset_password_universal, name='reset_password_universal'),
	path('login/', login_user, name='login_user'),
	path('logout/', logout_user, name='logout_user'),
	path('register/', register_user, name='register_user'),
	path('forgotpassword/', forgot_password, name='forgot_password'),
	path('activate/<slug:token>/', account_confirmed, name='account_confirmed'),
]