from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class employee_record(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_fname = models.CharField(max_length=100)
    emp_lname = models.CharField(max_length=100)
    emp_email = models.CharField(max_length=100)
    emp_phone = models.IntegerField()
    emp_address = models.CharField(max_length=250)
    emp_designation = models.CharField(max_length=100)

    def __str__(self):
        
        return str(self.emp_id)
    
class time_off_table(models.Model):
    Timeoff_id= models.AutoField(primary_key=True)
    timeoff_available= models.TextField()
    emp_fname=models.CharField(max_length=100)
    emp_lname=models.CharField(max_length=100)
    emp_id=models.ForeignKey(employee_record,on_delete=models.CASCADE, null=True)

class schedule_table(models.Model):
    schedule_id=models.AutoField(primary_key=True)
    emp_id=models.ForeignKey(employee_record,on_delete=models.CASCADE, null=True)
    assigned_schedule=models.DateTimeField()
    total_hours=models.DecimalField(max_digits=5, decimal_places=2)
    emp_fname=models.CharField(max_length=100)
    emp_lname=models.CharField(max_length=100)
    emp_designation = models.CharField(max_length=100, null=True)
    timeoff_id=models.ForeignKey(time_off_table,on_delete=models.CASCADE, null=True)
 
class timing_table(models.Model):
    timing_table_id=models.AutoField(primary_key=True)
    emp_id=models.ForeignKey(employee_record,on_delete=models.CASCADE,null=True)
    punch_in=models.TimeField(auto_now_add=True, null=True)
    punch_out=models.TimeField(auto_now_add=True, null=True)
    break_start=models.TimeField(auto_now_add=True, null=True)
    break_end=models.TimeField(auto_now_add=True, null=True)
    working_day=models.DateField(auto_now_add=True,null=True)

class payroll_table(models.Model):
    payroll_table_id=models.AutoField(primary_key=True)
    fk_emp_id=models.ForeignKey(employee_record,on_delete=models.CASCADE,null=True)
    emp_sin=models.IntegerField()
    emp_account_Number=models.BigIntegerField()
    emp_payrate=models.DecimalField(max_digits=5, decimal_places=2)
    pay_cycle=models.SmallIntegerField(default=1)
    fk_schedule_id=models.ForeignKey(schedule_table,on_delete=models.CASCADE,null=True)


class Events(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()







