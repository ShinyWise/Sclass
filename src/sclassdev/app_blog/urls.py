from django.urls import path
from .views import view


urlpatterns = [
    path('blog/', view, name='app_blog')
]