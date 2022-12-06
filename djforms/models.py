from django.db import models
        
class Simple(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        app_label = 'djforms'
