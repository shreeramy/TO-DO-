from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


app_name = 'board'

# router = DefaultRouter()
# router.register(r'board', views.BoardViewSet, basename='board')
# urlpatterns = router.urls

urlpatterns = [
	path('', views.BoardView.as_view()),
	path('<pk>', views.BoardOperations.as_view()),
	path('tasks/<pk>', views.TaskView.as_view()),
	path('task/<pk>', views.TaskOperation.as_view()),
	path('task-status/<pk>', views.TaskStatus.as_view())
]