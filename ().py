# coding: utf-8
from hexlet_django_blog.article.models import Article
a = Article()
a.name = 'my super article'
a.body = 'my content'
a.name
a.id
a.created_at
a = Article.objects.create(name='my super article', body='my content')
a.created_at
b = Article.objects.create(name='my super article B', body='my content is best')
c = Article.objects.create(name='hello boys', body='my content is my content')
d = Article.objects.create(name='hello guys', body='my my my my')
e = Article.objects.create(name='peace', body='go to street')
a = Article.objects.all()
a.name
a.body
Article.objects.get(id=1)
Article.objects.get(id=2)
d.name
a.name
a = Article.objects.create(name='my super article', body='my content')
c.name
a.name
