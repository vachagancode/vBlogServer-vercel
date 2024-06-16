from django.urls import path, include
from . import views

app_name = "posts"

urlpatterns = [
	path('posts/get_posts/', views.getPosts),
	path('posts/get_posts/<int:pk>/', views.getSpecialPost),
	path('posts/edit_posts/<int:pk>/', views.editSpecificPost),
	path('posts/add_posts/', views.addPosts),
	path('posts/delete_post/<int:pk>/', views.deletePost),
]