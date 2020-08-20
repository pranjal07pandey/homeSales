from django.db import models

# Create your models here.

class Agent(models.Model):
    fname = models.CharField(max_length = 100, default='')
    lname = models.CharField(max_length = 100, default='')
    joined_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = "gallery", blank =True)
    house_sold = models.IntegerField(default=0)
    is_mvp = models.BooleanField(default=False)

    def __str__(self):
        return self.fname + self.lname


class Home(models.Model):
    agent = models.ForeignKey(Agent, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100, default = '')
    location = models.CharField(max_length = 100, default = '')
    no_of_rooms = models.IntegerField(default=0)
    area = models.DecimalField(default=0, decimal_places=4, max_digits=19)
    price = models.DecimalField(default = 0, decimal_places=2, max_digits=19)
    image1 = models.ImageField(upload_to = "gallery", blank = False)
    image2 = models.ImageField(upload_to = "gallery", blank = True)
    image3 = models.ImageField(upload_to = "gallery", blank = True)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length = 100, default='', blank=False)
    phone = models.CharField(max_length= 100, default = '', blank=False)
    home_selected = models.CharField(max_length= 100, default = '', blank=False)
    email = models.EmailField(blank= True)
    message = models.TextField(max_length=250, blank=True)


    def __str__(self):
        return self.name + self.home_selected


