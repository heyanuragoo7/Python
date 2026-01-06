from rest_framework import serializers
from .models import User, Blog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "email", "password", "age")

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("name", "content", "owner")
