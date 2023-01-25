from django.urls import path
from predictClass import views

app_name='predictClass'
urlpatterns = [
    path('', views.IndexView, name="IndexView"),
    path('predict/', views.predicts, name='predicts'),
]
