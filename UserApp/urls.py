from django.conf.urls import url
from .views import UsersList, UserDetail

urlpatterns = [
    url('', UsersList.as_view()),
    url('<int:pk>/', UserDetail.as_view()),
]
