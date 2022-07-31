# Generated by Django 4.0.6 on 2022-07-31 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_book_amortfinish_valid_book_costfinish_valid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='cost_for',
            new_name='calculate_depreciation',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='costfirstvalid',
            new_name='cost_begining_period',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='amortfirst_valid',
            new_name='depreciation_begining_period',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='amortfinish_valid',
            new_name='depreciation_end_period',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='finish_valid',
            new_name='price_end_period',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='costfinish_valid',
            new_name='residual_value',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='costfinish_validone',
            new_name='residual_value_begining',
        ),
        migrations.RemoveField(
            model_name='book',
            name='cost_first',
        ),
        migrations.AddField(
            model_name='book',
            name='initial_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Первоначальная стоимость'),
        ),
        migrations.AlterField(
            model_name='book',
            name='add_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата поставки'),
        ),
        migrations.AlterField(
            model_name='book',
            name='adoption',
            field=models.EmailField(blank=True, max_length=75, verbose_name='Дата принятия к учету'),
        ),
        migrations.AlterField(
            model_name='book',
            name='number',
            field=models.IntegerField(default=False, verbose_name='Инвентарный номер'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Наименование оборудования'),
        ),
    ]
