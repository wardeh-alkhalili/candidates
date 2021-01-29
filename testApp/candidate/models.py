from django.db import models
from .validators import validate_file_extension
# Create your models here.
class Candidate(models.Model):
    class Departments(models.TextChoices):
        HR = 'HR',
        IT = 'IT', 
        FINANCE = 'Finance'
    
    email=models.CharField(default='' ,max_length=300)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    year_of_experience=models.IntegerField()
    departmnet_Id=models.CharField(max_length=10,choices=Departments.choices,default=Departments.IT)
    resume = models.FileField(default='',upload_to='http://documents/', validators=[validate_file_extension])
