from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=225)
    pub_date = models.DateField()
    body = models.TextField()
    url = models.CharField(max_length=225)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        if len(self.body) <= 40:
            return self.body
        else:
            return self.body[:85] + "...."
