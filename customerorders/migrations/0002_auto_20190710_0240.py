# Generated by Django 2.2.1 on 2019-07-09 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerorders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='order_details',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='product_code',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='serial_no',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='warranty',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='warranty_type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
