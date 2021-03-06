# Generated by Django 2.2 on 2019-09-23 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_product_visible_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_creation',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, default=False, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.FileField(blank=True, default=False, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.FileField(blank=True, default=False, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
