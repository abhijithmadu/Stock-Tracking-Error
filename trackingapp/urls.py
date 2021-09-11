from django.urls import path

from . import views

urlpatterns = [
    path('', views.sample, name='sample'),
    # path('api_data/', views.api_data, name='api_data'),
]