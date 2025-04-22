from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions
from .models import Vote
from .serializers import VoteSerializer
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count

class VoteCreateView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

class VoteResultsTodayView(APIView):
    def get(self, request):
        today = timezone.now().date()
        results = (
            Vote.objects.filter(created_at=today)
            .values("menu__id", "menu__restaurant__name")
            .annotate(votes=Count("id"))
            .order_by("-votes")
        )
        return Response(results)
