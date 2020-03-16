from django.db import models


class Account(models.Model):

    nick_name  = models.CharField(max_length=50)
    email      = models.CharField(max_length=200, unique=True)
    password   = models.CharField(max_length=300)
    like       = models.ManyToManyField('space.Space', through='Like')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'accounts'


class Host(models.Model):
    nick_name   = models.CharField(max_length=50)
    email       = models.CharField(max_length=200, unique=True)
    password    = models.CharField(max_length=300)
    phonenumber = models.CharField(max_length=11, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hosts'


class Reservation(models.Model):
    user       = models.ForeignKey('Account', on_delete=models.SET_NULL, null=True)
    confirm    = models.BooleanField(null=True)
    space      = models.ForeignKey('space.Space', on_delete=models.SET_NULL, null=True)
    host       = models.ForeignKey('Host', on_delete=models.SET_NULL, null=True)
    year       = models.CharField(max_length=10)
    month      = models.CharField(max_length=10)
    day        = models.CharField(max_length=10)
    hour       = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reservations'


class Like(models.Model):
    user       = models.ForeignKey('Account', on_delete=models.SET_NULL, null=True)
    space      = models.ForeignKey('space.Space', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'likes'
