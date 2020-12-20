from django.db import models
item =( 
    ("1", "Raw Rice"), 
    ("2", "Wheat"), 
    ("3", "Sugar"), 
    ("4", "Atta"), 
    ("5", "Urad dal"), 
    ("6", "Rava"), 
    ("7", "Coconut oil"), 
    ("8", "Sunflower oil"), 
    ("9", "Salt"), 
    ("10", "Green gram"), 
    ("11", "Black chana"), 
    ("12", "Chilly powder"), 
    ("13", "Soap"), 
    ("14", "Coriander powder"), 
    ("15", "Tea"), 
    ("16", "Fenugreek"), 
    ("17", "Dal"), 
    ("18", "Mustard"), 
    ("19", "Tur dal"), 
    ("20", "Maida") 
)
# Create your models here.
class Survey(models.Model):
    combination = models.CharField(max_length = 20,default="0")
    item1 = models.CharField(max_length = 20, choices = item,default="") 
    item2 = models.CharField(max_length = 20, choices = item,default="") 
    item3 = models.CharField(max_length = 20, choices = item,default="") 
    item4 = models.CharField(max_length = 20, choices = item,default="") 
    item5 = models.CharField(max_length = 20, choices = item,default="") 
    item6 = models.CharField(max_length = 20, choices = item,default="") 
    item7 = models.CharField(max_length = 20, choices = item,default="") 
    item8 = models.CharField(max_length = 20, choices = item,default="") 
    item9 = models.CharField(max_length = 20, choices = item,default="") 
    item10 = models.CharField(max_length = 20, choices = item,default="")  

    def __str__(self):
        return self.combination