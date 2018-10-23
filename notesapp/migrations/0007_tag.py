# Generated by Django 2.1.2 on 2018-10-23 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0006_personalnote_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
                ('personal_note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notesapp.PersonalNote')),
            ],
        ),
    ]
