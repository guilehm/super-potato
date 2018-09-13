from django.urls import path

from core import views

app_name = 'core'


urlpatterns = [
    path('', views.index, name='index'),
    path('assistance/patient/list/', views.patient_list, name='patient-list'),
]
