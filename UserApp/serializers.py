from rest_framework import serializers
from UserApp.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'firstname', 'lastname', 'email', 'posts_count')

    def create(self, validated_data):
        return User.objects.create(**validated_data)
