from django.urls import path
from . import views

urlpatterns = [
	path('', views.PostView.as_view()),
	path('<int:pk>/', views.PostDetail.as_view()),
	path('reviews/<int:pk>/', views.AddComment.as_view(), name='add_comment'),
	path('<int:pk>/add_like/', views.AddLike.as_view(), name='add_like'),
	path('<int:pk>/remove_like/', views.RemoveLike.as_view(), name='remove_like')
]
