
from django.db import models
from set.models import Set

class Flashcard(models.Model):
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    side_one = models.TextField() 
    side_two = models.TextField()
    star = models.BooleanField(default=False)





