from rest_framework import serializers
from .models import Restaurant, Menu

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name"]

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "restaurant", "date", "items"]

    def validate(self, data):
        # Проверяем, что меню на эту дату у ресторана ещё нет
        if Menu.objects.filter(restaurant=data["restaurant"], date=data["date"]).exists():
            raise serializers.ValidationError("Menu for this restaurant and date already exists.")
        return data
