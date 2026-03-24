from django.urls import path
from .views import summarize_view

urlpatterns = [
    path("summaries/", summarize_view),
]
