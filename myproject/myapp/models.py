from django.db import models

class FreeTable(models.Model):
    car_no = models.CharField(max_length=255)
    reason = models.CharField(max_length=255, blank=True, null=True)
    other = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'freetable'  # 明确指定数据库表名
