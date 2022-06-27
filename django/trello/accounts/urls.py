from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
	path('forgot-password', views.ForgotPassword.as_view()),
	path('forgot_password/<uidb64>/<token>', views.forgot_password,
         name='forgot_password'),
	path('signup', views.SignUp.as_view()),
	path('change-password', views.ChangePassword.as_view()),
	path('profile', views.UserProfile.as_view()),
]