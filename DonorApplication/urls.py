from django.contrib import admin
from django.urls import path
from User_panel import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home,name="Home"),
    path("login/", views.Request,name="Request"),
    # path("login/", auth_views.LoginView.as_view(template_name='login.html'), name="Request"),
    path("donorDetails/", views.Search,name="Search"),
    path("registration/", views.Register,name="Register"),
    path("forgetPassword/", views.ForgetPass, name="ForgetPassword"),
    path("signup", views.Signup, name="Signup"),
    path("bloodrequest/", views.RequestPage, name="BloodRequest"),
    path("", views.SendMessage, name="SendMessage")
]
