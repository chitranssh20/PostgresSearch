from django.db import models

# Create your models here.
class Book(models.Model):
    title: models.CharField(max_length = 1000, db_index= True, null = False)
    author: models.CharField(max_length= 5000)

    
#   class Meta:
#       indexes = [  
#           GinIndex(name='NewGinIndex', fields=['title'], opclasses=['gin_trgm_ops']),
#       ]

