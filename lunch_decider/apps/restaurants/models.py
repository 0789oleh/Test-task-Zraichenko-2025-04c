from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
  
    def __str__(self) -> str:
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey("restaurants.Restaurant", on_delete=models.CASCADE, related_name="menus")
    date = models.DateField()
    items = models.JSONField()  # Можно заменить на related модель, если хочешь гибкости

    class Meta:
        unique_together = ("restaurant", "date")
        ordering = ["-date"]

    def __str__(self):
        return f"Menu for {self.restaurant.name} on {self.date}"
