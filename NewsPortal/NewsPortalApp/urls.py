from django.urls import path
from .views import *


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('<int:pk>', CommentList.as_view()),
    path('<int:pk>', CommentDetail.as_view()),
    path('search/', PostSearch.as_view()),
]
