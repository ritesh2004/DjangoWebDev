from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='home'),
    path('create/', views.create, name='create'),
    path('view/',views.view, name='view'),
    path('addQuiz/', views.addQuiz, name="addQuiz"),
    path('submit/', views.submit, name="submit"),
]