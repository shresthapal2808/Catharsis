from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_step2, name='register'),
    path('welcome/', views.welcome_page, name='welcome'),
    path('survey/', views.survey, name='survey'),


    #unfinished pages 
    path('connect/', views.unfinished_page, name='connect'),
    path('community/', views.unfinished_page, name='community'),
    path('about/', views.unfinished_page, name='about'),

    #footer
    path('faq/', views.unfinished_page, name='faq'),
    path('support/', views.unfinished_page, name='support'),
    path('blog/', views.unfinished_page, name='blog'),
    path('self-help/', views.unfinished_page, name='self-help'),
    path('emergency/', views.unfinished_page, name='emergency'),
    path('policy/', views.unfinished_page, name='policy'),
    path('terms/', views.unfinished_page, name='terms'),
    path('careers/', views.unfinished_page, name='careers'),
    path('contact_us/', views.unfinished_page, name='contact_us'),

]
