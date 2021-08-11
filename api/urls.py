from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

app_name='api'


urlpatterns = [
    path('register',user_views.registerUser,name="registerUser"),
    path('login',auth_views.LoginView.as_view(template_name='frontend/login.html'),name="loginUser"),
    path('logout',auth_views.LogoutView.as_view(template_name='frontend/logout.html'),name="logoutUser"),
    path('search-user',user_views.searchUser,name="searchUser"),
    path('create-blog',user_views.createBlog,name="create-blog"),
]