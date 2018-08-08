from django.db import models


# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=30, default='John')
    last_name = models.CharField(max_length=30, default='Doe')
    # full_name = models.CharField(max_length=61)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='clients')
    dob = models.DateField(null=True, blank=True)

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.get_full_name()