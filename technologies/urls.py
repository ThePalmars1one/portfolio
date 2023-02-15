from django.urls import path
from .views import tech_views

urlpatterns = [
    path('', tech_views, name="tech")
]

