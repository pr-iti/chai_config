from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
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


# 1 to many relationship
class chai_Review(models.Model):
    chai = models.ForeignKey(chai_menu,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    data_added = models.DateTimeField(default=timezone.now)
     

    def __str__(self):

        return f"{self.user.username} reviewed for {self.chai.name}"
    

# many to many relationship

class store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varities = models.ManyToManyField(chai_menu,related_name='stores')

    def __self__(self):
        return self.name
    

# 1 to 1 r/n
class chai_Certificate(models.Model):
    chai = models.OneToOneField(chai_menu,on_delete=models.CASCADE,related_name='certificate')
    cerificate_no = models.CharField(max_length=100)
    issue_date = models.DateTimeField(timezone.now())
    valid_untill = models.DateTimeField()
    def __self__(self):
        return f"certificate for {self.name.chai}"