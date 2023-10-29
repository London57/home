from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings




# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=15)
#     birth_date = models.DateField(null=True, blank=True)

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    
    def __str__(self):
        return self.username


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')


    def __str__(self):
        return self.name

    class Meta: 
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


class Bd(models.Model):
    
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')


    def __str__(self):  
        return f'{self.title} за {int(self.price)}'

    class Meta: 
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']
    

class comment(models.Model):
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Bd', on_delete=models.CASCADE)
    text = models.TextField(max_length=250)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ['published']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        # indexes = [
        #     models.Index(fields=['created']),
        #     ]

        


