# Generated by Django 2.2.1 on 2019-07-06 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20190706_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='scheduled_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='stop_date',
            field=models.DateField(null=True),
        ),
    ]