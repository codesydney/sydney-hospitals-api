#from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Hospital
from .serializers import HospitalSerializer

class HospitalList(generics.ListCreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class HospitalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
