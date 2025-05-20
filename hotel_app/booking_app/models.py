from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Hotel(models.Model):

    hotel_id=models.IntegerField(primary_key=True)
    hotel_name=models.CharField(max_length=64)
    hotel_location=models.CharField(max_length=60)
    hotel_rating=models.IntegerField()
    price_per_night=models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return f"Hotel_ID: {self.hotel_id}, Hotel_name: {self.hotel_name}, Hotel_location : {self.hotel_location}, Hotel_rating : {self.hotel_rating}, Price_per_night : {self.price_per_night}"

# class Login(models.Model): # Started to create a login page model (include create new account and have it link to a create page)

# Create
