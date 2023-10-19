from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Like
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

        return redirect(f'/{pk}')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # вытаскиваем IP адрес нашего клиента
    else:
        ip = request.META.get('REMOTE_ADDR')  # IP с которого к нам поступил запрос, хорошо в том случае, если клиент использует сторонние ресурсы

    return ip


class AddLike(View):
    """
        Добавление лайка
    """

    def get(self, request, pk):
        ip_client = get_client_ip(request)

        try:
            Like.objects.get(ip=ip_client, post_id=pk)

            return redirect(f'/{pk}')

        except:
            new_like = Like()
            new_like.ip = ip_client
            new_like.post_id = int(pk)

            new_like.save()

            return redirect(f'/{pk}')


class RemoveLike(View):
    """
        Удаление лайка
    """

    def get(self, request, pk):
        ip_client = get_client_ip(request)

        try:
            cur_like = Like.objects.get(ip=ip_client)
            cur_like.delete()

            return redirect(f'/{pk}')

        except:
            return redirect(f'/{pk}')
