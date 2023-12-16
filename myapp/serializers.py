from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=70)
    email=serializers.EmailField(max_length=100)
    password=serializers.CharField(max_length=100)