from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.post_list_create_api_view),
    path('posts/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view()),
    path('comments/', views.CommentListCreateAPIView.as_view()),
    path('comments/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view()),
]
