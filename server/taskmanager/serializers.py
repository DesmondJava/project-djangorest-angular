from django.contrib.auth.models import User
from rest_framework import serializers

from server.taskmanager.models import Task, Answer


class TaskSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    class Meta:
        model = Task
        fields = ("title", "description", "created_date", "finish_date", "author", "priority", "private", "likes")


class AnswerSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Store model """
    class Meta:
        model = Answer
        fields = ("text", "created_date", "task", "author")


class UserSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Employee model """
    class Meta:
        model = User
        fields = ("username", "email")
