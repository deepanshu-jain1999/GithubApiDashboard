from rest_framework import serializers
from .models import GithubUser


class UserSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = GithubUser