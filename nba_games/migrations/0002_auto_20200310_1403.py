# Generated by Django 3.0.3 on 2020-03-10 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba_games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='home_score',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='visitor_score',
            field=models.IntegerField(null=True),
        ),
    ]