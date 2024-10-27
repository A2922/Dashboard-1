from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class transactiontypes(models.Model):
    TRANSACTIONS_TYPE = [
        ('SA', 'SAVING ACCOUNT'),
        ('CA', 'CURRENT ACCOUNT'),
        ('LA', 'LOAN ACCOUNT'),

    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='trans/')
    date_added = models.DateTimeField(default=timezone.now)
    types = models.CharField(max_length=2, choices=TRANSACTIONS_TYPE)
    description = models.TextField(default ='empty')
    def __str__(self):
        return self.name 
    
    # one to many
class transaction_details(models.Model):
    transaction = models.ForeignKey(transactiontypes, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, in_delete=models.CASCADE)
    ratings = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return  f'{self.user.username} review for {self.transaction.name}'
    
    #Many to many

    class Store(models.Model):
        name = models.CharField(max_length=100)
        location = models.CharField(max_length=100)
        char_varities = models.ManyToManyField(transactiontypes, related_name='stores')

        def __str__(self):
            return self.name
        