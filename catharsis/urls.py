from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_step2, name='register'),
    path('welcome/', views.welcome_page, name='welcome'),
    path('survey/', views.survey, name='survey'),
    path('about/', views.about, name='about'),
    path('therapy/audio/', views.audio_therapy, name='audio_therapy'),
    path('therapy/video/', views.video_therapy, name='video_therapy'),
    path('therapy/chat/', views.chat_therapy, name='chat_therapy'),
    path('listeners/profile/', views.listener_profile, name='listener_profile'),
    path('listeners/ratings/', views.listener_ratings, name='listener_ratings'),
    path('listeners/experience/', views.listener_experience, name='listener_experience'),
    path('community/', views.community, name='community'),
    




    #unfinished pages 
    path('connect/', views.unfinished_page, name='connect'),

    #listeners
    path('listener_ratings/', views.unfinished_page, name='listener_ratings'),
    path('listener_experience/', views.unfinished_page, name='listener_experience'),

    #therapy
    path('audio/', views.unfinished_page, name='audio_therapy'),
    path('video/', views.unfinished_page, name='video_therapy'),
    path('chat/', views.unfinished_page, name='chat_therapy'),

    

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
