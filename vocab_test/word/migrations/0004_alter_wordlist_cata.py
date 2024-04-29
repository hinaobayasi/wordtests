# Generated by Django 5.0.3 on 2024-03-28 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0003_alter_wordlist_cata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordlist',
            name='cata',
            field=models.CharField(choices=[('verb', '動詞'), ('nouns', '名詞'), ('adjective', '形容詞'), ('adverb', '副詞'), ('others', 'その他'), ('phrase', '熟語')], max_length=100, verbose_name='品詞'),
        ),
    ]
