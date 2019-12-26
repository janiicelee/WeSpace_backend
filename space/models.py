from django.db import models

class Space_Categories(models.Model):
    category = models.CharField(max_length=200)

    class Meta:
        db_table = 'space_categories'
