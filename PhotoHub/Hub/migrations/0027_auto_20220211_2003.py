# Generated by Django 3.1.6 on 2022-02-11 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hub', '0026_photographer_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='img',
        ),
        migrations.AddField(
            model_name='blog',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
