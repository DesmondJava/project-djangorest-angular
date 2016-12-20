from rest_framework import viewsets
from taskmanager.models import User, Task, Answer
from taskmanager.serializers import UserSerializer, TaskSerializer, AnswerSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Store objects """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


