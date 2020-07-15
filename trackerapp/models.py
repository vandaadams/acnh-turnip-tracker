from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Turnip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    day_choice = (
        ('0', 'Monday'),
        ('1', 'Tuesday'),
        ('2', 'Wednesday'),
        ('3', 'Thursday'),
        ('4', 'Friday'),
        ('5', 'Saturday'),
    )
    day = models.CharField(max_length=10, choices=day_choice, default='Monday')
    time_choice = (
        ('M', 'Morning'),
        ('E', 'Evening'),
    )
    time = models.CharField(max_length=10, choices=time_choice, default='Morning')
    price = models.IntegerField(blank=False, validators=[
            MaxValueValidator(700),
            MinValueValidator(0)
        ])

    def __str__(self):
        return self.day

#################  chart #################

class ZingChartConfig(models.Model):
    title = models.CharField(max_length = 50)
    xAxis = models.CharField(max_length = 20)
    yAxis = models.CharField(max_length = 20)
    theme = models.CharField(max_length = 20)

    class Meta:
        db_table = "zingchart_config"

class ZingChartSeriesData1(models.Model):
    time = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        db_table = "zingchart_data_1"
