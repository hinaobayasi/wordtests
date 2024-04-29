# Generated by Django 5.0.3 on 2024-04-27 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0007_delete_color_wordliste_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordliste',
            name='phrase',
            field=models.CharField(default=' ', max_length=300, verbose_name='MINIMAL PHRASES'),
        ),
        migrations.AddField(
            model_name='wordliste',
            name='yaku',
            field=models.CharField(default=' ', max_length=200, verbose_name='日本語訳'),
        ),
    ]