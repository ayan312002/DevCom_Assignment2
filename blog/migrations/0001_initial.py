# Generated by Django 3.0.3 on 2020-03-25 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200)),
                ('article_content', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
            ],
        ),
    ]
