from django.db import models

# Create your models here.
from django.db import models


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    in_stock = models.IntegerField(default=0)
    descr = models.CharField(max_length=255)
    price = models.FloatField()
    picture = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'books'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=30)
    login = models.CharField(max_length=20)
    passwd = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'users'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    amount = models.IntegerField()
    order_date = models.DateField()
    pay_date = models.DateField()
    deliv_date = models.DateField()
    status = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'orders'
