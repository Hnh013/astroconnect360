# Generated by Django 3.0 on 2020-07-21 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_tarotarticle_tarotquestion_yearlytarot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarotarticle',
            name='banner',
        ),
        migrations.AlterField(
            model_name='tarotarticle',
            name='content',
            field=models.TextField(),
        ),
    ]