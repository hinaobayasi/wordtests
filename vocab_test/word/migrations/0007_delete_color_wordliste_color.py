# Generated by Django 5.0.3 on 2024-04-20 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0006_rename_wordlist_wordliste'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.AddField(
            model_name='wordliste',
            name='color',
            field=models.CharField(choices=[('赤', '赤'), ('黄', '黄'), ('青', '青')], default='赤', max_length=20, verbose_name='色'),
        ),
    ]
