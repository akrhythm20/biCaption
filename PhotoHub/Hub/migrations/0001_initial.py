# Generated by Django 3.1.6 on 2022-01-28 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('state', models.CharField(choices=[('AN', 'Andaman and Nicobar Islands'), ('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chhattisgarh'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('DL', 'Delhi'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('LA', 'Ladakh'), ('LD', 'Lakshadweep'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OD', 'Odisha'), ('PB', 'Punjab'), ('PY', 'Pondicherry'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TS', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UK', 'Uttarakhand'), ('WB', 'West Bengal')], default=None, max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=200)),
                ('pincode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('Male', '1'), ('Female', '0')], default='1', max_length=10)),
                ('dob', models.DateTimeField()),
                ('category', models.CharField(choices=[('Event', 'Event'), ('Fashion', 'Fashion'), ('Sports', 'Sports'), ('Food', 'Food'), ('Art and Portrait', 'Art and Portrait'), ('Architecture', 'Architecture'), ('Documentary', 'Documentary'), ('Travel', 'Travel'), ('Modelling and Lifestyle', 'Modelling and Lifestyle'), ('Nature and Wildlife', 'Natue and Wildlife'), ('Product', 'Product'), ('Photo Journalism', 'Photo journalism')], max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('AN', 'Andaman and Nicobar Islands'), ('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chhattisgarh'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('DL', 'Delhi'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('LA', 'Ladakh'), ('LD', 'Lakshadweep'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OD', 'Odisha'), ('PB', 'Punjab'), ('PY', 'Pondicherry'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TS', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UK', 'Uttarakhand'), ('WB', 'West Bengal')], default='AN', max_length=50)),
                ('pincode', models.IntegerField()),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Busy', 'Busy')], default='Available', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('payment_status', models.BooleanField(blank=True, null=True)),
                ('Photographer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Hub.photographer')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hub.customer')),
            ],
        ),
    ]
