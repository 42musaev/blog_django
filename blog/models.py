from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone


class Article(models.Model):
    title = models.CharField('Загаловок', max_length=256)
    img = models.ImageField('Изоброжение', upload_to='article_img')
    text = models.TextField('Текст')
    date_pub = models.DateTimeField('Дата публкиации', default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
