# Generated by Django 4.1.1 on 2022-10-26 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab1', '0002_remove_books_author_books_in_stock_alter_books_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.FloatField(),
        ),
    ]