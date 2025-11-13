from django.db import models

# Create your models here.
class DZ_News_post(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_discription = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_data = models.DateTimeField('Дата публикации')
    avtor = models.CharField('Автор публикации', max_length=70)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'