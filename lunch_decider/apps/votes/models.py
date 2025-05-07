from django.db import models

# Create your models here.

from django.db import models

class Vote(models.Model):
    employee = models.ForeignKey("employees.Employee", on_delete=models.CASCADE, related_name="votes")
    menu = models.ForeignKey("restaurants.Menu", on_delete=models.CASCADE, related_name="votes")
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("employee", "created_at")
        verbose_name = "Vote"
        verbose_name_plural = "Votes"

    def __str__(self):
        return f"{self.employee} voted for {self.menu} on {self.created_at}"
