# Generated by Django 3.1.5 on 2021-02-12 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yyApp', '0004_auto_20210211_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='postID',
        ),
        migrations.AddField(
            model_name='board',
            name='petID',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='yyApp.pet'),
        ),
    ]
