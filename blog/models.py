from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'  # значение - метка
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)  # varchar
    slug = models.SlugField(max_length=250)  # так же varchar
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # при CASCADE удаление пользователя, удалит связанные с ним статьи

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ['-publish']  # сортировка по полю даты публикации в обратном порядке (сначала новые посты)


    def __str__(self):
        return self.title

