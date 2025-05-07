from rest_framework import serializers
from .models import Vote
from apps.employees.models import Employee
from apps.restaurants.models import Menu
import datetime

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ("id", "employee", "menu", "created_at")
        read_only_fields = ("created_at",)

    def validate(self, data):
        employee = data["employee"]
        today = datetime.date.today()
        if Vote.objects.filter(employee=employee, created_at=today).exists():
            raise serializers.ValidationError("You have already voted today.")
        return data

    def create(self, validated_data):
        # Создание нового экземпляра Employee
        return Restaurant.objects.create(**validated_data)
