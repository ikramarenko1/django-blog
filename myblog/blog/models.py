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
