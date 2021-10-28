from django.db import models

class employee(models.Model):
    empID = models.CharField(max_length=20)
    empName = models.CharField(max_length=100)
    empEmail= models.EmailField()
    password=models.CharField(max_length=100)
    empAddress = models.CharField(max_length=15)
    class Meta:
        db_table = "employee"