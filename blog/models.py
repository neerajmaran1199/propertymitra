
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

TENANT_TYPES = (
    ('boys','BOYS'),
    ('girls', 'GIRLS'),
    ('family','FAMILY'),
    ('single','BOYS/GIRLS'),
    ('all','ALL TYPE'),
   
)

HOUSE_TYPES = (
    ('all','all'),
    ('1bhk', '1 BHK'),
    ('2bhk','2 BHK'),
    ('3bhk','3 BHK'),
    ('sinle room','SINGLE ROOM'),
   
)





class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='blog_pics')
    location = models.CharField(max_length=20)
    area = models.CharField(max_length=40)
    status = models.CharField(max_length=10)
    description = models.CharField(max_length=70)
    rent = models.IntegerField()
    mobile_number = models.IntegerField()
    
    tenant = models.CharField(max_length=10, choices=TENANT_TYPES, default='all')
    house = models.CharField(max_length=10, choices=HOUSE_TYPES, default='all')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})