from rest_framework import serializers
from .models import GithubUser
from django.utils import timezone


class UserSearchSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(UserSearchSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = GithubUser
        fields = '__all__'

    def create(self, validated_data):
        instance = GithubUser.objects.create(**validated_data)
        return instance

