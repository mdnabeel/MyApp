from django.db import models

# Create your models here.


class Status(models.Model):
    class Meta:
        verbose_name_plural = "Status"

    cur_status = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.cur_status


class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()
    dob = models.DateField()
    address = models.TextField()
    acc_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    date_of_deactivation = models.DateField(null=True, blank=True)
