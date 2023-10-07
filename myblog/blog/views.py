from django.shortcuts import render
from django.views.generic.base import View
from .models import Post

# Create your views here.


class PostView(View):
    '''
    Вывод записей
    '''

    def get(self, request):
        posts = Post.objects.all()
        
        return render(request, 'blog/blog.html', {'posts': posts})
