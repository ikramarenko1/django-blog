from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm


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
    

class AddComment(View):
    """
    Добавление комментария
    """
    
    def post(self, request, pk):
        form = CommentsForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()

        return redirect('/{pk}')