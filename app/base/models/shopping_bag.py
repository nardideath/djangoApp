from django.db import models
from django.contrib.auth.models import User


class ShoppingBag(models.Model):
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    
    quantity = models.IntegerField(
        default=1
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"ShoppingBag {self.id} for user {self.user.username}"