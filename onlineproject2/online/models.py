from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
<<<<<<< HEAD
        return self.username
        
=======
        return self.username
>>>>>>> 9f023d7cbe350bd2a4c39eeee844c5839d636faf
