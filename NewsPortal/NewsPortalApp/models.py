from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.SmallIntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.author_user.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.rating_author = pRat * 3 + cRat
        self.save()
    
    def ___str___(self):
        return f'{self.author_user}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)

    def ___str___(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    author_connect = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOISES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )
    category_type = models.CharField(max_length=2, choices=CATEGORY_CHOISES, default=ARTICLE)

    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


class PostCategory(models.Model):
    post_through = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_through = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['date_create']

    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.comment_user)


