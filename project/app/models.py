from django.db import models

# Create your models here.
class Students(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.CharField(max_length=50)
    stu_contact=models.IntegerField()
    stu_password=models.CharField(max_length=25)

    def __str__(self):
        return self.stu_name
    
class myQuery(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.CharField(max_length=50)
    stu_query=models.CharField(max_length=50)
    def __str__(self):
        return self.stu_email
