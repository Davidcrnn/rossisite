# Generated by Django 2.2 on 2019-09-30 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20190923_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]