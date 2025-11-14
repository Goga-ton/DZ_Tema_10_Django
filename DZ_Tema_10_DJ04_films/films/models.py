from django.db import models

# Create your models here.
class Films_stat(models.Model):
    title = models.CharField('Название фильма', max_length=50)
    description = models.TextField('Описание фильма')
    feedback = models.CharField('Отзыв', max_length=200)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'