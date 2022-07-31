from django.db import models
from .user import User
class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    date = models.DateTimeField()
    totalsale = models.IntegerField(default=0)
    
    