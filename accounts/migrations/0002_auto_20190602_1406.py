# Generated by Django 2.2.1 on 2019-06-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='admin status'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(default=False, verbose_name='manager status'),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
