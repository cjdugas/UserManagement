__author__ = 'Carolyn Dugas'
from rest_framework import serializers
from service.models import Log, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'created_at', 'updated_at')


class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = ('id', 'user_id', 'action', 'attributes', 'created_at')


