from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=65, unique=True)
    # False 代表女
    sex = models.BooleanField(default=False)
    icon = models.ImageField(upload_to='icons',null=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'ttsx_users'


class UserTicket(models.Model):
    user = models.ForeignKey(User)
    ticket = models.CharField(max_length=255)
    out_time = models.DateTimeField()

    class Meta:
        db_table = 'ttsx_users_ticket'
