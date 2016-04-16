
# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from task.settings import MEDIA_ROOT


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Название')

    def __unicode__(self):
        return u'%s' % (self.name)
    class Meta:
        verbose_name = u'Категории'


class News(models.Model):
    category = models.ForeignKey(Category, to_field='id', db_column='parameter',
                                  on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'Рубрика')
    name = models.CharField(max_length=200, verbose_name=u'Заголовок')
    text = models.CharField(max_length=1000, verbose_name=u'Текст')
    date = models.DateField(verbose_name=u'Дата публикации')
    photo = models.FileField(upload_to=MEDIA_ROOT, max_length=100, verbose_name=u'Фото')
    votes = models.IntegerField(default=0, verbose_name=u'Рейтинг')

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = u'Новости'



#-----------------------------------------------------
class NewsForm(ModelForm):
    class Meta:
        model = News

class CategoryForm(ModelForm):
    class Meta:
        model = Category

