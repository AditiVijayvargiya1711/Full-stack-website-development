from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.home,name="home"),
    path("signinsite/",views.signinsite,name="signin"),
    path("signin_login/",views.signin_login,name="signin_login"),
    path("loginsite/",views.loginsite,name="login"),
    path("upload/",views.upload,name="upload"),
    path("profile1/",views.profile1,name="profile1"),
    path("profile2/",views.profile2,name="profile2"),
    path("profile3/",views.profile3,name="profile3"),
    path("saveprofile/",views.saveprofile,name="saveprofile"),
    path("upload1/",views.upload1,name="upload1"),
    path("updateprofile/",views.updateprofile,name="updateprofile")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)