from django.urls import path
from .views import HospitalList, HospitalDetail

urlpatterns = [
    path('hospitals/', HospitalList.as_view(), name='hospital-list'),
    path('hospitals/<int:pk>/', HospitalDetail.as_view(), name='hospital-detail'),
]
