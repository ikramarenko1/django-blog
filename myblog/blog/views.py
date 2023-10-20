from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .models import Post, Like
from .form import CommentsForm


# Create your views here.
class PostView(View):
    """
    Вывод записей
    """

    def get(self, request):
        posts = Post.objects.all().order_by('-date')

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


class ToggleLike(View):
    """
        Добавление лайка
    """

    def post(self, request, pk):
        ip_client = get_client_ip(request)
        post = get_object_or_404(Post, pk=pk)

        try:
            like = Like.objects.get(ip=ip_client, post=post)
            like.delete()

            liked = False
        except Like.DoesNotExist:
            new_like = Like(ip=ip_client, post=post)
            new_like.save()

            liked = True

        like_count = post.like_set.count()

        return JsonResponse({'liked': liked, 'like_count': like_count})


class CheckLikeStatus(View):
    """
    Проверка статуса лайка на посте при загрузке
    """

    def post(self, request):
        ip_client = get_client_ip(request)
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, pk=post_id)

        try:
            like = Like.objects.get(ip=ip_client, post=post)
            liked = True
        except Like.DoesNotExist:
            liked = False

        like_count = post.like_set.count()

        return JsonResponse({'liked': liked, 'like_count': like_count})
