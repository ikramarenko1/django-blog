from django.db import models


class Post(models.Model):
    title = models.CharField('Название записи', max_length=100)
    description = models.TextField('Содержимое записи')
    author = models.CharField('Автор', max_length=50)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изображение публикации', upload_to='image/%Y-%m/', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        

class Comment(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    content = models.TextField('Текст комментария', max_length=1000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)  # Когда удаляется объект публикации, все комментарии связаны с публикацией тоже удаляются
    
    def __str__(self) -> str:
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
