from django.urls import path
from .views import view


urlpatterns = [
    path('landing/', view, name='app_landing')
]