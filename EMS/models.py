from django.db import models

# Create your models here.
class emp(models.Model):
    id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=20)
    emp_contact_no = models.CharField(max_length=10)
    emp_address = models.CharField(max_length =20)
    emp_designation = models.CharField(max_length=20)
    dept = models.ForeignKey("department",on_delete=models.CASCADE)
   

class department(models.Model):
    id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=20)
   

class project(models.Model):
    id = models.AutoField(primary_key=True)
    p_description = models.CharField(max_length=20)
    dept = models.ForeignKey("department",on_delete=models.CASCADE)
   

class emp_wfh(models.Model):
    id = models.AutoField(primary_key=True)
    emp = models.ForeignKey("emp",on_delete=models.CASCADE)
    wfh_salary = models.IntegerField()
    

class emp_os(models.Model):
    id = models.AutoField(primary_key=True)
    emp = models.ForeignKey("emp",on_delete=models.CASCADE)
    os_salary = models.IntegerField()
    

class leave(models.Model):
    id = models.AutoField(primary_key=True)
    l_description = models.CharField(max_length=20)
    

class takes(models.Model):
    id = models.AutoField(primary_key=True)
    emp = models.ForeignKey("emp",on_delete=models.CASCADE)
    l = models.ForeignKey("leave",on_delete=models.CASCADE)
    t_date = models.DateField()
    t_retdate = models.DateField()
    l_available = models.IntegerField()
    

