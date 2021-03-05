from django.db import models
from datetime import datetime, timedelta


class Article(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)


class Author(models.Model):
    name = models.CharField(max_length=120)


class Reader(models.Model):
    name = models.CharField(max_length=120)


class Book(models.Model):
    name = models.CharField(max_length=120)
    year_of_public = models.DateField()
    author = models.ManyToManyField(Author)
    book_reserved = models.ForeignKey(Reader, on_delete=models.CASCADE, null=True, blank=True)


class User(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.TextField(max_length=100)
    Description = models.TextField(max_length=500, null=True, blank=True)
    author_post = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class CommentPost(models.Model):
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=150, null=True, blank=True)
    comment_to_comment = models.ForeignKey('myapp.CommentPost', null=True, blank=True, on_delete=models.DO_NOTHING)


class LikeComment(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    like_comment = models.ForeignKey(CommentPost, on_delete=models.CASCADE)


class DisslikeComment(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    DisslikeComment = models.ForeignKey(CommentPost, on_delete=models.CASCADE)


class LikePost(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    like_post = models.ForeignKey(Post, on_delete=models.CASCADE)


class DisslikePost(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    Disslike_post = models.ForeignKey(Post, on_delete=models.CASCADE)

