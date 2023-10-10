from django.shortcuts import render
from django.views.generic.base import View
from .models import Post


# Create your views here.
class PostView(View):
    """
    Вывод записей
    """

    def get(self, request):
        posts = Post.objects.all()

        return render(request, 'blog/blog.html', {'posts': posts})


class PostDetail(View):
    """
    Отдельная страница для записи
    """

    def get(self, request, pk):
        post = Post.objects.get(id=pk)

        return render(request, 'blog/blog_post.html', {'post': post})
