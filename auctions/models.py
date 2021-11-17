from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass





class Listing(models.Model):
    title = models.CharField(max_length = 999)

    description = models.TextField()
    starting_bid = models.FloatField()
    active = models.BooleanField(blank = False, default = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "owner")
    category = models.CharField(blank = True, max_length = 999)
    img_url = models.URLField(blank = True)
    winner = models.ForeignKey(User, blank = True, on_delete = models.CASCADE, related_name = "new_owner", null = True)
    
    def __str__(self):
        return (f"{self.title} - {self.description} : $ {self.starting_bid}")

class Bid(models.Model):
    value = models.FloatField()
    listing = models.ForeignKey(Listing, verbose_name = "price", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    winner = models.BooleanField(default = False)
    
    def __str__(self):
        return (f"Bid $ {self.value} for {self.listing}")

class Comment(models.Model):
    content = models.TextField()
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE)
    
    user = models.ForeignKey(User, on_delete = models.CASCADE)


class Watchlist(models.Model):
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE, blank = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = False)