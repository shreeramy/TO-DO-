from rest_framework import serializers
from . models import Board, Task


class BoardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Board
		fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):

	class Meta:
		model = Task
		fields = (
			'pk',
			'user',
			'name',
			'description',
			'created_at',
			'board',
			'status'
		)
