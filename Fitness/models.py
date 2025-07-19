from django.db import models


class Yoga(models.Model):
    client_name=models.CharField(max_length=40)
    client_age=models.IntegerField(default=0)
    loction=models.CharField(max_length=50)
    gender=models.CharField(max_length=40)
    contact_number=models.CharField(max_length=40)
    fees=models.IntegerField(default=0)
    

    def __str_(self):
        return self.client_name


