from django.db import models


class TM_MAIN_DATA(models.Model):
    DT = models.CharField(max_length=20)
    RED_BALL = models.CharField(max_length=200)
    BLUE_BALL = models.CharField(max_length=10)


class TA_DATA_RESULT(models.Model):
    DT = models.CharField(max_length=20)
    SOURCE_DATA = models.CharField(max_length=50)
    RED_S_BALL = models.BigIntegerField()
    BLUE_BALL = models.BigIntegerField()
    CHA = models.CharField(max_length=50)
    HE = models.BigIntegerField()
    JI = models.BigIntegerField()
