from account.models import Hosts, Accounts

from django.db      import models


class Spaces(models.Model):
    title = models.CharField(max_length=100)
    short_intro = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    long_intro = models.TextField()
    location = models.CharField(max_length=300)
    host = models.ForeignKey('account.Hosts', on_delete=models.SET_NULL, null=True)
    min_time = models.CharField(max_length=10, null=True)
    min_guest = models.CharField(max_length=10, null=True)
    open_time = models.CharField(max_length=10)
    close_time = models.CharField(max_length=10)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    amenities = models.ManyToManyField(
        'Amenities', through='SpaceAmenities')

    class Meta:
        db_table = 'spaces'

class Amenities(models.Model):
    amenity   = models.CharField(max_length       = 300)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now     = True)

    class Meta:
        db_table = 'amenities'

class Holiday(models.Model):
    holiday = models.DateTimeField()
    space = models.ForeignKey('Spaces', on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'holiday'

class SpaceCategories(models.Model):
    category  = models.CharField(max_length       = 200)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now     = True)

    class Meta:
        db_table = 'space_categories'

class Notices(models.Model):
    notice    = models.CharField(max_length           = 300)
    space     = models.ForeignKey('Spaces', on_delete = models.SET_NULL, null = True)
    create_at = models.DateTimeField(auto_now_add     = True)
    update_at = models.DateTimeField(auto_now         = True)

    class Meta:
        db_table = 'notice'

class SpaceAmenities(models.Model):
    amenity = models.ForeignKey('Amenities', on_delete=models.SET_NULL, null=True)
    space = models.ForeignKey('Spaces', on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'spaces_amenities'


class Qeustion(models.Model):
    space = models.ForeignKey('Spaces', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('account.Accounts', on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Mata:
        db_table = 'questions'

class Reviews(models.Model):
    user      = models.ForeignKey(Accounts, on_delete = models.SET_NULL, null = True)
    space     = models.ForeignKey(Spaces, on_delete   = models.SET_NULL, null = True)
    content   = models.TextField()
    image     = models.URLField(max_length            = 2500)
    create_at = models.DateTimeField(auto_now_add     = True)
    update_at = models.DateTimeField(auto_now         = True)

    class Meta:
        db_table = 'reviews'

class Tags(models.Model):
    tag       = models.CharField(max_length         = 30)
    space     = models.ForeignKey(Spaces, on_delete = models.SET_NULL, null = True)
    create_at = models.DateTimeField(auto_now_add   = True)
    update_at = models.DateTimeField(auto_now       = True)

    class Meta:
        db_table = 'tags'

class Images(models.Model):
    space_image = models.URLField(max_length          = 2500)
    space       = models.ForeignKey(Spaces, on_delete = models.SET_NULL, null = True)
    create_at   = models.DateTimeField(auto_now_add   = True)

    class Meta:
        db_table = 'images'
