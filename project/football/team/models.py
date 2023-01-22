from django.db import models

# Create your models here.
class Football(models.Model):
    first_name = models.CharField(max_length=45)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.first_name

class Football_Team(models.Model):
    club = models.ForeignKey(Football, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=45)
    description = models.CharField(max_length=256)
    release_date = models.DateField() 

    def __str__(self):
        return self.first_name
