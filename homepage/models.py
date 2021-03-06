from django.db import models

class Reservation_Rest(models.Model):
    fullname=models.CharField(max_length=50);
    email=models.EmailField(max_length=100)
    date=models.DateField();
    time=models.TimeField();
    party_size=models.IntegerField(default=0);
    phone_no=models.CharField(max_length=30);

    class Meta:
        unique_together=(('fullname','date','time','phone_no'));
    def __str__(self):
        return self.fullname;

class Drinks_Item(models.Model):
    name=models.CharField(max_length=100);
    price=models.IntegerField(default=0);
    content=models.CharField(max_length=500);

    def __str__(self):
        return self.name;

class FastFood_Item(models.Model):
    name=models.CharField(max_length=100);
    price=models.IntegerField(default=0);
    content=models.CharField(max_length=500);

    def __str__(self):
        return self.name;

class Food_Item(models.Model):
    name=models.CharField(max_length=100);
    price=models.IntegerField(default=0);
    content=models.CharField(max_length=500);

    def __str__(self):
        return self.name;


class Order_main(models.Model):
    name=models.CharField(max_length=100);
    total=models.IntegerField(default=0);
    def __str__(self):
        return self.name;

class Order_secondary(models.Model):
    food_name=models.CharField(max_length=50);
    price=models.IntegerField(default=0);
    foreign_id=models.ForeignKey('Order_main',on_delete=models.CASCADE);
    def __str__(self):
        return self.food_name;
