from django.db import models

# Create your models here.

class chai_menu(models.Model):

    CHAI_TYPES = [
        ('ms', 'masala'),
        ('gr', 'ginger'),
        ('el', 'elachi'),
        ('hb', 'herbal'),
        ('ch', 'choco')
    ]
    name=models.CharField(max_length=30)
    image = models.ImageField (upload_to='uploads/')
    description = models.TextField(max_length=100)
    price = models.IntegerField()
    type = models.TextField(default='',choices=CHAI_TYPES)

    # to populate what should be seen on the frontend
    def __str__(self):
        return self.name
    


class chai_stores(models.Model):

    CHAI_TYPES = [
        ('ms', 'mansarowar'),
        ('gn', 'Girdhari nagar'),
        ('sn', 'shyam nagar'),
        ('ch', 'chaupad'),
        ('bh', 'chapra')
    ]
    name=models.CharField(max_length=30)
   
    description = models.TextField(max_length=100)
    distance = models.IntegerField()
    type = models.TextField(default='',choices=CHAI_TYPES)

    # to populate what should be seen on the frontend
    def __str__(self):
        return self.name
