from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.Item_name
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    Item_name = models.CharField(max_length=200)
    Item_desc = models.CharField(max_length=200)
    Item_price = models.IntegerField()
    Item_image = models.CharField(max_length=500, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQxBwsiy_mCHZ6dHERdZlKhYGL3Gw5QlOUiw&usqp=CAU")


    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})