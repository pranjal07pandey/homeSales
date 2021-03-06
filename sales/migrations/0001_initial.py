# Generated by Django 3.0.8 on 2020-08-20 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='', max_length=100)),
                ('lname', models.CharField(default='', max_length=100)),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
                ('house_sold', models.IntegerField(default=0)),
                ('is_mvp', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=100)),
                ('home_selected', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('message', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('location', models.CharField(default='', max_length=100)),
                ('no_of_rooms', models.IntegerField(default=0)),
                ('area', models.DecimalField(decimal_places=4, default=0, max_digits=19)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('image1', models.ImageField(upload_to='gallery')),
                ('image2', models.ImageField(blank=True, upload_to='gallery')),
                ('image3', models.ImageField(blank=True, upload_to='gallery')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Agent')),
            ],
        ),
    ]
