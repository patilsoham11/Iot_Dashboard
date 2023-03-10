# Generated by Django 3.2.16 on 2022-12-02 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Info',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=10)),
                ('company_address', models.CharField(max_length=50)),
                ('company_logo', models.ImageField(default='', upload_to='images')),
                ('company_image', models.ImageField(default='', upload_to='images')),
                ('created_date', models.DateField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('deleted_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Details',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=12, unique=True)),
                ('address', models.CharField(max_length=50)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.company_info')),
            ],
        ),
        migrations.CreateModel(
            name='Device_Details',
            fields=[
                ('device_id', models.AutoField(primary_key=True, serialize=False)),
                ('device_name', models.CharField(max_length=20)),
                ('time_stamp', models.TimeField(auto_now_add=True)),
                ('installed_date', models.DateField()),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.company_info')),
            ],
        ),
        migrations.CreateModel(
            name='Alert_Master',
            fields=[
                ('alert_master_id', models.AutoField(primary_key=True, serialize=False)),
                ('alert_massage', models.CharField(max_length=20)),
                ('register', models.IntegerField()),
                ('counts', models.IntegerField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.device_details')),
            ],
        ),
        migrations.CreateModel(
            name='Alert_Data',
            fields=[
                ('alart_id', models.AutoField(primary_key=True, serialize=False)),
                ('device_id', models.IntegerField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('iot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.company_info')),
            ],
        ),
    ]
