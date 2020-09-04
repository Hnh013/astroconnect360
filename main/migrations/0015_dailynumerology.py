# Generated by Django 3.0 on 2020-07-21 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_kundli'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyNumerology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], max_length=50)),
                ('date', models.DateField()),
                ('content', models.TextField()),
                ('astroprofile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Astro_Profile')),
            ],
        ),
    ]