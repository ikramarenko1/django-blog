from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .models import Post, Like
from .form import CommentsForm, PostForm
from .utils import get_client_ip

from datetime import date


class AddPost(View):
    """
    Добавление новой записи
    """

    def get(self, request):
        # Отображение формы для создания новой записи
        return render(request, 'blog/add_post.html')

    def post(self, request):
        # Обрабатываем отправленную форму и сохраняем новую запись
        ip_client = get_client_ip(request)
        form = PostForm(request.POST, request.FILES)  # Создаем форму на основе отправленных данных

        if form.is_valid():
            post = form.save(commit=False)  # Сохраняем форму, но пока не коммитим в базу
            post.ip = ip_client
            post.date = date.today()

            post.save()  # Коммитим в базу

            # Перенаправляем пользователя на страницу новой записи
            return redirect(f'/{post.id}')

        else:
            # Если есть ошибки в форме, возвращаем ее обратно с этими ошибками
            return render(request, 'blog/add_post.html', {'form': form})


class EditPost(View):
    """
    Редактирование существующей записи
    """

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # Получаем запись по первичному ключу или возвращаем ошибку 404
        form = PostForm(instance=post)  # Создаем форму на основе этой записи

        return render(request, 'blog/edit_post.html', {'form': form})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save()

            # Перенаправляем на страницу этого поста
            return redirect(f'/{pk}')
        else:
            # Если форма содержит ошибки, возвращаем ее с этими ошибками
            return render(request, 'blog/edit_post.html', {'form': form})


class DeletePost(View):
    """
    Удаление записи
    """

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # Получаем запись по первичному ключу или возвращаем ошибку 404
        post.delete()  # Удаляем запись

        # Перенаправляем на главную страницу
        return redirect('/')


class PostView(View):
    """
    Вывод записей
    """

    def get(self, request):
        posts = Post.objects.all().order_by('-date')  # Получаем все записи и сортируем их по дате

        return render(request, 'blog/blog.html', {'posts': posts})


class PostDetail(View):
    """
    Отдельная страница для записи
    """

    def get(self, request, pk):
        post = Post.objects.get(id=pk)  # Получаем запись по ID

        current_ip = get_client_ip(request)  # Получаем IP-адрес текущего пользователя, для проверки его ли пост
        context = {
            'post': post,
            'current_ip': current_ip
        }

        return render(request, 'blog/blog_post.html', context)
    

class AddComment(View):
    """
    Добавление комментария
    """
    
    def post(self, request, pk):
        form = CommentsForm(request.POST)  # Создаем форму на основе отправленных данных

        if form.is_valid():
            form = form.save(commit=False)  # Сохраняем, но пока не коммитим в базу
            form.post_id = pk  # Устанавливаем связь с записью блога
            form.save()  # Коммитим

        return redirect(f'/{pk}')


class ToggleLike(View):
    """
        Добавление лайка
    """

    def post(self, request, pk):
        ip_client = get_client_ip(request)
        post = get_object_or_404(Post, pk=pk)

        # Пытаемся получить лайк этого пользователя для этой записи
        try:
            like = Like.objects.get(ip=ip_client, post=post)
            like.delete()

            liked = False

        # Если лайка нет, создаем новый
        except Like.DoesNotExist:
            new_like = Like(ip=ip_client, post=post)
            new_like.save()

            liked = True

        # Считаем общее количество лайков для этой записи
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

        # Пытаемся получить лайк этого пользователя для этой записи
        try:
            like = Like.objects.get(ip=ip_client, post=post)
            liked = True
        except Like.DoesNotExist:
            liked = False

        # Считаем общее количество лайков для этой записи
        like_count = post.like_set.count()

        return JsonResponse({'liked': liked, 'like_count': like_count})
