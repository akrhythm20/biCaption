# Generated by Django 4.0.1 on 2022-02-06 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hub', '0020_alter_appointment_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
