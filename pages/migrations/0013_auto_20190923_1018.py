# Generated by Django 2.2 on 2019-09-23 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20190923_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_creation',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='visible_home',
            field=models.BooleanField(default=True),
        ),
    ]
