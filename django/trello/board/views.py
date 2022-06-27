from django.shortcuts import render
from . serializers import BoardSerializer, TaskSerializer
from . models import Board, Task
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


class BoardView(APIView):
	def get(self, request):
		board_object = Board.objects.filter(user=request.user)
		return Response(BoardSerializer(board_object, many=True).data, status=status.HTTP_200_OK)

	def post(self, request):
		board_object = Board.objects.create(
			name=request.data.get('name'),
			desscription=request.data.get('description'),
			user=request.user
		)
		return Response({'message': "Board created successfully!"})


class BoardOperations(APIView):
	def get(self, request, pk):
		board_object = Board.objects.get(pk=pk)
		return Response(BoardSerializer(board_object).data, status=status.HTTP_200_OK)

	def delete(self, request, pk):
		board_object = Board.objects.filter(pk=pk)
		board_object.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def put(self, request, pk):
		board_object = Board.objects.filter(pk=pk)
		board_object.update(
			name=request.data.get('name'),
			desscription=request.data.get('desscription')
		)
		return Response(status=status.HTTP_200_OK)


class TaskView(APIView):
	def get(self, request, pk):
		board_object = Board.objects.filter(pk=pk)
		board_data = BoardSerializer(board_object.first()).data
		task_object = Task.objects.filter(user=request.user, board__pk=pk)
		done = TaskSerializer(task_object.filter(status="DONE"), many=True).data
		todo = TaskSerializer(task_object.filter(status="TODO"), many=True).data
		inprogress = TaskSerializer(task_object.filter(status="INPROGRESS"), many=True).data
		return Response({"done": done, "todo": todo, "inprogress": inprogress,
						 "board": board_data}, status=status.HTTP_200_OK)

	def post(self, request, pk):
		task_object = Task.objects.create(
			name=request.data.get('name'),
			description=request.data.get('description'),
			user=request.user,
			board=Board.objects.get(pk=pk)
		)
		return Response({'message': "Task created successfully!"})


class TaskOperation(APIView):
	def delete(self, request, pk):
		task_object = Task.objects.filter(user=request.user, pk=pk)
		task_object.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def put(self, request, pk):
		task_object = Task.objects.filter(user=request.user, pk=pk)
		task_object.update(
			name=request.data.get('name'),
			description=request.data.get('description')
		)
		return Response({'message': "Task updated successfully!"})


class TaskStatus(APIView):
	def put(self, request, pk):
		task_object = Task.objects.filter(user=request.user, pk=pk)
		task_object.update(
			status=request.data.get('status')
		)
		return Response({'message': "Task status changed successfully!"})

