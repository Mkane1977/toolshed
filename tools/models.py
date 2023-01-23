from django.db import models


class Toolshed(models.Model):
    
    tool = models.ForeignKey('Tool',on_delete= models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Tool(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=500)
    type = models.CharField(max_length=200)
    charger = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name + ' ' + self.model + ' ' + self.type + ' ' + self.charger


   
    
