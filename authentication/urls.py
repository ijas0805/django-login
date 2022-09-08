from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('reset', views.reset, name="reset"),
    path('mail_reverification', views.mail_reverification, name="mail_reverification"),
    #path('changepass', views.changepass, name="changepass"),
    path('changepass/<uidb64>/<token>', views.changepass, name='changepass'),
    path('verifynewpass/<uidb64>/<token>', views.verifynewpass, name="verifynewpass"),
]