from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

from PostApp.models import Post
from PostApp.serializers import PostSerializer, PostWriteSerializer

# Create your views here.
from UserApp.models import User
from demo_app.WorkerApp.tasks import add


class PostsList(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        add.delay(5, 7)
        return Response(serializer.data)

    def post(self, request):
        user = User.objects.get(id=request.data.get("user"))
        serializer = PostWriteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.save(user=user)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
