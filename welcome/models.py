from django.db import models

from django.core.validators import MinValueValidator ,MaxValueValidator, MinLengthValidator

# Validators is like rules 

class Inventory(models.Model):

    


    name = models.CharField(max_length=40, validators= [MinLengthValidator(1)])

    location = models.CharField(max_length=50)

    Current_Quantity=models.FloatField(validators=[MinValueValidator(1)])  

    min_Level=models.IntegerField(validators=[MinValueValidator(1)])  

    expiry_date =models.DateField(null=True, blank=True)

    status = models.CharField(max_length=50, default="In Stock")
    Price = models.FloatField(default=5,validators=[MinValueValidator(0.5)])


    def __str__(self):
        return f"{self.name} ({self.Current_Quantity}) ({self.Price})"


        # when you update the Schema you have to update the Database as well