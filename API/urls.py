from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='api-index'),
    path('prediction', views.RequestPrediction.as_view(), name='api-prediction'),
]