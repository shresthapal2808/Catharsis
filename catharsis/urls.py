from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_step2, name='register'),
    path('welcome/', views.welcome_page, name='welcome'),
    path('survey/', views.survey, name='survey'),
]
