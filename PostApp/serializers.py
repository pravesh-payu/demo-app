from rest_framework import serializers
from PostApp.models import Post
from UserApp.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'user')

    def create(self, validated_data):
        return Post.objects.create(**validated_data)


class PostWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'user')

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
