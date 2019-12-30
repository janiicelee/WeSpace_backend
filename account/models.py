from django.db import models


class Accounts(models.Model):

    nick_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=300)
    like = models.ManyToManyField('space.Spaces', through='Likes')
    nick_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'accounts'


class Hosts(models.Model):
    nick_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hosts'


class Likes(models.Model):

    user = models.ForeignKey('Accounts', on_delete=models.SET_NULL, null=True)
    space = models.ForeignKey(
        'space.Spaces', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'likes'
