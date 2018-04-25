from django.db import models

class Ad(models.Model):
    advertiser = models.CharField(max_length=2000)
    email_id = models.EmailField()
    name = models.CharField(max_length=2000)
    video = models.CharField(max_length=2000)
    banner = models.CharField(max_length=200)
    start_date = models.DateTimeField('Date Ad Starts')
    end_date = models.DateTimeField('Date Ad Ends')
    play_count = models.IntegerField(default=0, editable=False)
    touch_count = models.IntegerField(default=0, editable=False)
    play_duration = models.IntegerField(editable=False, default=0)

    def __str__(self):
        "Set to display advertiser name in the ads table"

        return self.advertiser


class Campaign(models.Model):
    name = models.CharField(max_length=2000)
    playlist = models.ManyToManyField(Ad)

    def __str__(self):
        return self.name


class Device(models.Model):
    pass
