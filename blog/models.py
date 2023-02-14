from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Model Post"""
    authonr = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=u'Автор'
    )

    title = models.CharField(
        max_length=200,
        verbose_name=u'Заголовок'
    )

    text = models.TextField(
        verbose_name=u'Текст'
    )

    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name=u'Дата_создания'
    )

    published_date = models.DateTimeField(
        blank=True, null=True,
        verbose_name=u'Дата_публикации'
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
