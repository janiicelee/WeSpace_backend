from django.db import models

class Accounts(models.Model):
    nick_name  = models.CharField(max_length = 50)
    email      = models.CharField(max_length = 200, unique = True)
    password   = models.CharField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'accounts'

class Hosts(models.Model):
    nick_name  = models.CharField(max_length = 50)
    email      = models.CharField(max_length = 200, unique = True)
    password   = models.CharField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'hosts'