# Generated by Django 3.2.8 on 2021-10-31 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_alter_favorited_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorited',
            options={'verbose_name': 'Избранные рецепты', 'verbose_name_plural': 'Избранные рецепты'},
        ),
    ]
