from django.forms import ModelForm  # Импортируем формы Django
from .models import ArticleComment, Article


class ArticleCommentForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['content']


"""
РУЧНАЯ ВАЛИДАЦИЯ ФОРМЫ

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True -> типо NULL)
    description = forms.CharField(max_length=200, required=True)

    class Meta:
        model = Category
        fields = ['name', 'description', 'state']
"""


class ArticleEditForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
