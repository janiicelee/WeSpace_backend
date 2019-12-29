from django.db import models
from account.models import Hosts


class Spaces(models.Model):
    title = models.CharField(max_length=100)
    short_intro = models.CharField(max_length=200)
    long_intro = models.TextField()
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()
    host = models.ForeignKey(Hosts, on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'spaces'


class Amenities(models.Model):
    amenity = models.CharField(max_length=300)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'amenities'


class Space_Categories(models.Model):
    category = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'space_categories'


class Qeustion(models.Model):
    space = models.ForeignKey(
        'Spaces', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(
        'account.Accounts', on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Mata:
        db_table = 'question'
