from django.db import models


class Spaces(models.Model):
    title = models.CharField(max_length=100)
    short_intro = models.CharField(max_length=200)
    long_intro = models.TextField()
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()
    host = models.ForeignKey(
        'account.Hosts',
        on_delete=models.SET_NULL,
        null=True)
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


class Images(models.Model):
    space_image = models.URLField(max_length=2500)
    space = models.ForeignKey('Spaces', on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'images'


class Categories_Space(models.Model):
    space = models.ForeignKey(Spaces, on_delete=models.SET_NULL, null=True)
    space_category = models.ForeignKey(
        'Space_Categories',
        on_delete=models.SET_NULL,
        null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories_space'
