from django.db import models

class DataName(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    summary_file = models.CharField(db_column='Summary_file', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.TimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    test_name = models.CharField(db_column='Test_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    test_date = models.DateField(db_column='Test_date', blank=True, null=True)  # Field name made lowercase.
    test_time = models.TimeField(db_column='Test_time', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    log_file = models.CharField(max_length=255, blank=True, null=True)
    html_report = models.CharField(max_length=255, blank=True, null=True)
    video_file = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_name'
        ordering = ['time']