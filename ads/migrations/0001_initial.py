# Generated by Django 2.0.4 on 2018-04-25 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertiser', models.CharField(max_length=2000)),
                ('email_id', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=2000)),
                ('video', models.CharField(max_length=2000)),
                ('banner', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(verbose_name='Date Ad Starts')),
                ('end_date', models.DateTimeField(verbose_name='Date Ad Ends')),
                ('play_count', models.IntegerField(default=0, editable=False)),
                ('touch_count', models.IntegerField(default=0, editable=False)),
                ('play_duration', models.IntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('playlist', models.ManyToManyField(to='ads.Ad')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
