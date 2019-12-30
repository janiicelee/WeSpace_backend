from django.db import models
from account.models import Hosts, Accounts


class Spaces(models.Model):
    from account.models import Hosts
    title = models.CharField(max_length=100)
    short_intro = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    long_intro = models.TextField()
    open_time = models.CharField(max_length=10)
    close_time = models.CharField(max_length=10)
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


class Reviews(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.SET_NULL, null=True)
    space = models.ForeignKey(Spaces, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    image = models.URLField(max_length=2500)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reviews'
