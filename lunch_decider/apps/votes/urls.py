from django.urls import path
from .views import VoteCreateView, VoteResultsTodayView

urlpatterns = [
    path("votes/", VoteCreateView.as_view(), name="vote-create"),
    path("votes/today/", VoteResultsTodayView.as_view(), name="vote-results-today"),
]