from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user_id = models.OneToOneField(
            User,
            on_delete=models.CASCADE,
            primary_key=True,
            default=-1
            
    )
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    num_sets = models.IntegerField(default=0)


    def get_absolute_url(self):
        return reverse("user-profiles:user-profile", kwargs={"id": self.id})

    

