# Generated by Django 2.1.2 on 2018-10-23 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0004_personalnote'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalnote',
            name='private_content',
            field=models.TextField(blank=True),
        ),
    ]
