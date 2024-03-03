from django.urls import path

from polls.Views import prediction, prediction2, index, project, home

urlpatterns = [
    path('', home.home, name='home'),
    path('index/', index.index, name='index'),
    path('pro/', project.project, name='pro'),
    path('pred/', prediction.prediction, name='pred'),
    path('pred2/', prediction2.prediction2, name='pred2'),
]
