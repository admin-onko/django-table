# Generated by Django 4.0.6 on 2022-07-28 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_published_book_add_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='amortfinish_valid',
            field=models.IntegerField(blank=True, null=True, verbose_name='Амортизация на конец периода'),
        ),
        migrations.AddField(
            model_name='book',
            name='costfinish_valid',
            field=models.IntegerField(blank=True, null=True, verbose_name='Остаточная стоимость'),
        ),
    ]
