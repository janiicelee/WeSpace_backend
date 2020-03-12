from django.db      import models
from account.models import Host, Account


class Space(models.Model):
    title         = models.CharField(max_length=100)
    short_intro   = models.CharField(max_length=200)
    price         = models.DecimalField(max_digits=12, decimal_places=2)
    long_intro    = models.TextField()
    location      = models.CharField(max_length=300)
    host          = models.ForeignKey('account.Host', on_delete=models.SET_NULL, null=True)
    min_time      = models.CharField(max_length=10, null=True)
    min_guest     = models.CharField(max_length=10, null=True)
    open_time     = models.CharField(max_length=10)
    close_time    = models.CharField(max_length=10)
    create_at     = models.DateTimeField(auto_now_add=True)
    update_at     = models.DateTimeField(auto_now=True)
    amenity_space = models.ManyToManyField('Amenity', through='SpaceAmenity')

    class Meta:
        db_table = 'spaces'


class Amenity(models.Model):
    amenity    = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'amenities'


class Holiday(models.Model):
    holiday    = models.DateTimeField()
    space      = models.ForeignKey('Spaces', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'holidays'


class SpaceCategory(models.Model):
    category   = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'space_categories'


class Notice(models.Model):
    notice     = models.CharField(max_length=300)
    space      = models.ForeignKey('Spaces', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notices'


class SpaceAmenity(models.Model):
    amenity    = models.ForeignKey('Amenities', on_delete=models.SET_NULL, null=True)
    space      = models.ForeignKey('Spaces', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'space_amenities'


class Question(models.Model):
    space      = models.ForeignKey('Space', on_delete=models.SET_NULL, null=True)
    user       = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True)
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Mata:
        db_table = 'questions'


class Review(models.Model):
    user       = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    space      = models.ForeignKey(Space, on_delete=models.SET_NULL, null=True)
    content    = models.TextField()
    image      = models.URLField(max_length=2500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reviews'


class Tag(models.Model):
    tag        = models.CharField(max_length=30)
    space      = models.ForeignKey(Space, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tags'


class Image(models.Model):
    space_image = models.URLField(max_length=2500)
    space       = models.ForeignKey(Space, on_delete=models.SET_NULL, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'images'
