from django.urls import path
from . import views
from django.contrib.auth import views as authViews


urlpatterns = [
	path("signup/",views.signup,name="signup"),
	path("signin/",views.signin,name="signin"),
	path("singout/",views.signout,name="signout"),

	path("authLogin/",authViews.LoginView.as_view(template_name="authlogin.html"),name="login"),
	path("authLogout/",authViews.LogoutView.as_view(template_name="authlogout.html"),name="logout")
]