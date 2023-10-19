from django.urls import path
from . import views

urlpatterns = [
	path('', views.PostView.as_view()),
	path('<int:pk>/', views.PostDetail.as_view()),
	path('reviews/<int:pk>/', views.AddComment.as_view(), name='add_comment'),
	path('<int:pk>/toggle_like/', views.ToggleLike.as_view(), name='toggle_like'),
]
