# Generated by Django 2.0.4 on 2018-04-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='ad',
            name='banner',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='email_id',
            field=models.EmailField(default=None, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='name',
            field=models.CharField(default=None, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='play_duration',
            field=models.DurationField(default=None, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='start_date',
            field=models.DateTimeField(default=None, verbose_name='Date Ad Starts'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='touch_count',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='ad',
            name='video',
            field=models.CharField(default=None, max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='advertiser',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='ad',
            name='end_date',
            field=models.DateTimeField(verbose_name='Date Ad Ends'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='play_count',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]