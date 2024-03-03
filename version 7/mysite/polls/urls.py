from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pro/', views.project, name='pro'),
    path('pred/', views.prediction, name='pred'),
    path('pred2/', views.prediction2, name='pred2'),
]