from django.db import models

# Create your models here.
class filtermodel(models.Model):
	Name=models.CharField(max_length=30)
	Add=models.CharField(max_length=30)
	Dept=models.CharField(max_length=30)
	Sub=models.CharField(max_length=30)
	Date=models.DateField()