from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Blogs(model.Model);
 user = models.ForeignKey(User, on_delete=models.CASCADE)

text = models.TextField(max_length=200)
pic = models.ImageField(upload_to = 'pics/', blank=True, null= True)
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return f'{self.user.username} - {self.text[:10]}'
    


