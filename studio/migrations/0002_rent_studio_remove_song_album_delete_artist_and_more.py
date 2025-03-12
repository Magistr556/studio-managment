# Generated by Django 5.1.7 on 2025-03-12 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_date', models.DateTimeField()),
                ('rent_hours', models.IntegerField()),
                ('total_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('price_per_hour', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.DeleteModel(
            name='artist',
        ),
        migrations.AddField(
            model_name='rent',
            name='studio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studio.studio'),
        ),
        migrations.DeleteModel(
            name='album',
        ),
        migrations.DeleteModel(
            name='song',
        ),
    ]
