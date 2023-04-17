from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="home"),
    path('login/',views.loguser, name="loguser"),
    path('logout/',views.loguserOut,name="loguserOut"),
    path('signin/',views.SignIn,name="SignIn"),
    path('verify/', views.verify, name="verify"),
]
