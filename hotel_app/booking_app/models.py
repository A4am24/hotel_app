from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_id=models.IntegerField(primary_key=True)
    hotel_name=models.CharField(max_length=64)
    hotel_location=models.CharField(max_length=60)
    hotel_rating=models.IntegerField()

    def __str__(self):
        return f"Hotel_ID: {self.hotel_id}, Hotel_name: {self.hotel_name}, Hotel_location : {self.hotel_rating}, Hotel_rating : {self.hotel_rating}"
