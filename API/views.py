from django.http import response
from django.shortcuts import HttpResponse, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.conf import settings
import numpy as np

def index(request):
    return HttpResponse('<h1>Welcome to the api...</h1>')


class RequestPrediction(APIView):
    def get(self, request, form=None):
        return Response({'Response': 'Use this endpoint for predictions'})

    def post(self, request, form=None):
        try:
            data = request.data
            print(data)
            numpy_array = np.array(data)
            numpy_array = numpy_array/255
            input = numpy_array.reshape((1, numpy_array.shape[0], numpy_array.shape[0]))
            model = settings.ML_MODEL
            prediction = np.argmax(model.predict(input))
            return Response({'Prediction': prediction}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': 'model failed to produce prediction, please try again.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
