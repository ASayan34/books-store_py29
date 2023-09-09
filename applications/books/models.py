from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Book(models.Model):
    """
        Модель книги(книг)
    """
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book', verbose_name='Владаелец книги')
    title = models.CharField('Название' ,max_length=100)
    description = models.TextField('Описание', null=True, blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.title} --- {self.owner}'
    