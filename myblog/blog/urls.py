from django.urls import path
from . import views

urlpatterns = [
	path('', views.PostView.as_view()),
	path('<int:pk>/', views.PostDetail.as_view()),
	path('add_post/', views.AddPost.as_view(), name='add_post'),
	path('<int:pk>/edit/', views.EditPost.as_view(), name='edit_post'),
    path('<int:pk>/delete/', views.DeletePost.as_view(), name='delete_post'),
	path('reviews/<int:pk>/', views.AddComment.as_view(), name='add_comment'),
	path('<int:pk>/toggle_like/', views.ToggleLike.as_view(), name='toggle_like'),
	path('check_like_status/', views.CheckLikeStatus.as_view(), name='check_like_status'),
]
