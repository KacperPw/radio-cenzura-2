# Generated by Django 4.1.1 on 2023-03-06 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0005_postindex_author_postindex_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postindex',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
