# Generated by Django 3.1.5 on 2021-01-27 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210127_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer_tip',
            field=models.TextField(blank=True, null=True, verbose_name='Примечания'),
        ),
    ]
