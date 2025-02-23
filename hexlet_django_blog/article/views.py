from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from hexlet_django_blog.article.models import Article
from .forms import ArticleCommentForm, ArticleEditForm


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', {'article': article})


class ArticleCommentFormView(View):  # это класс из джанго???

    def get(self, request, *args, **kwargs):  # метод для обработки GET-запроса
        form = ArticleCommentForm()  # откуда берём форму
        # отправляем форму в шаблон
        return render(request, 'articles/form.html', {'form': form})
        # отправляем форму в шаблон

    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST)
        if form.is_valid():  # валидация данных
            form.save()  # сохранение формы

            # укажите нужное имя url для успешного редиректа
            return redirect('comment_success')

        return render(request, 'articles/form.html', {'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')  # получаем из запроса номер статьи
        article = Article.objects.get(id=article_id)  # ищем этот номер в БД

        # ниже, достаётся инфа из БД для редактирования
        form = ArticleEditForm(instance=article)
        return render(request, 'articles/update.html',
                      {'form': form, 'article_id': article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleEditForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')

        return render(request, 'articles/update.html',
                      {'form': form, 'article_id': article_id})


class ArticleFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('articles')
