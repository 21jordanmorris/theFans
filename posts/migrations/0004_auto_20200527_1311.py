# Generated by Django 3.0.6 on 2020-05-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sport',
            field=models.CharField(choices=[('NBA', 'NBA'), ('CFB', 'CFB'), ('NFL', 'NFL')], default='Null', max_length=25),
        ),
        migrations.AddField(
            model_name='post',
            name='writer',
            field=models.CharField(default='', max_length=255),
        ),
    ]
