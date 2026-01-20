from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Кастомная модель пользователя
    # username - уже создано в Абстрактном пользователе 
    # password - уже создано в Абстрактном пользователе
    # Добавим оптицональные поля
    # спец поле для почты EmailField
    email = models.EmailField(unique=True,null=False)
    # поле для большого количества текста(str)
    description = models.TextField()
    # поле для символом опр количества с ограничем максимум 255
    phone = models.CharField(max_length=11,unique=True,blank=True,null=True)
    # 2 вида поле для картинок
    avatar = models.ImageField(upload_to='avatars/')
    # Если вы храните не у себя в сервере картинки
    # храните их на удаленке или даете пользователю загрузить авар по ссылке
    image = models.URLField()

    # Добавляет флажок аутф группы людей 
    # и также задаем related name для избежания конфлитов 
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user',
        blank=True
    )

    def __str__(self):
        return self.username