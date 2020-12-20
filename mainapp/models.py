from django.db import models
from django.contrib.auth.models import AbstractUser


TYPE = ((1, 'enduser'),(2, 'ration store'),(3,'food-departmnet'))

class User(AbstractUser):
    email = models.EmailField( blank=False,max_length=254, verbose_name='email address')
    # ration_no = models.IntegerField()
    user_type = models.IntegerField(choices=TYPE,  default=1)
    is_Verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username
