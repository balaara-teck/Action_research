# Generated by Django 5.2.1 on 2025-06-18 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0005_rename_title_filemodel_researcher_filemodel_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='researcher',
            field=models.CharField(default='Untitled', max_length=200),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='topic',
            field=models.CharField(max_length=200),
        ),
    ]
