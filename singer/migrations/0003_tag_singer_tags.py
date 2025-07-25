# Generated by Django 4.2.20 on 2025-07-15 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singer', '0002_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='singer',
            name='tags',
            field=models.ManyToManyField(blank=True, to='singer.tag'),
        ),
    ]
