from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Article
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'created_at') # Перечисляем поля, отображаемые в таблице списка статей
    search_fields = ['name', 'body']  # Перечисляем поля для фильтрации

    list_filter = (('created_at', DateFieldListFilter),)
