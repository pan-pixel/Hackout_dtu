from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name = "home"),
    path('search',views.search, name = "search"),
    path('about',views.about, name = "about"),
    path('gamify',views.gameLearn,name='gameLearn'),
    path('goal',views.goal_analyser,name='goal'),
    path('syllabus',views.syllabus,name='syllabus'),
    path('lesson',views.lesson,name='lesson'),



]
