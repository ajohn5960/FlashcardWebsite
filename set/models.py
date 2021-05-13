from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Set(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    last_modified = models.DateTimeField()
    date_created = models.DateField(auto_now_add=True)
    last_studied = models.DateTimeField(null=True)
    is_private = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("sets:set_detail", kwargs={"set_id": self.id})







