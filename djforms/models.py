from django.db import models
        
class Simple(models.Model):
    name = models.CharField()

    class Meta:
        app_label = 'defaultapp'
