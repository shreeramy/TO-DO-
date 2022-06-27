from django.db import models
from accounts.models import UserAccount
# Create your models here.


class Board(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)
	user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, blank=True)
	desscription = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)


class Task(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)
	board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, blank=True)
	user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=50, default="TODO")
