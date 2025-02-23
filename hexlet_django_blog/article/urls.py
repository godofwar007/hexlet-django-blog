from django.urls import path
from hexlet_django_blog.article.views import IndexView, ArticleView
from hexlet_django_blog.article.views import ArticleCommentFormView
from hexlet_django_blog.article.views import ArticleFormEditView
from hexlet_django_blog.article.views import ArticleFormDeleteView


urlpatterns = [
    path('', IndexView.as_view(), name='articles'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(),
         name='article_update'),
    path('<int:id>/', ArticleView.as_view(), name='article_show'),
    path('new_comment/', ArticleCommentFormView.as_view(),
         name='comment_create'),
    path('<int:id>/delete/', ArticleFormDeleteView.as_view(),
         name='article_delete'),

]
