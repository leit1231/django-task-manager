from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    priority = models.IntegerField(verbose_name="Приоритет")
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    is_done = models.BooleanField(default=False, verbose_name="Статус выполнепия")
    deadline = models.DateTimeField(verbose_name="Дедлайн")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
