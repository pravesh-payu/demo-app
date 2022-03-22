from django.conf.urls import url
from .views import PostsList, PostDetail

urlpatterns = [
    url('', PostsList.as_view()),
    url('<int:pk>/', PostDetail.as_view()),
]
