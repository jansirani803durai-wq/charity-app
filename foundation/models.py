from django.db import models
class Donation(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField()
    address=models.TextField()
    amount=models.CharField(max_length=30)
    custom_amount=models.PositiveIntegerField(null=True, blank=True)
    cause=models.CharField(max_length=120)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'{self.name} - {self.amount} - {self.cause}'
class Volunteer(models.Model):
    full_name=models.CharField(max_length=120)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    interest=models.CharField(max_length=100)
    availability=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.full_name
class ContactMessage(models.Model):
    name=models.CharField(max_length=120, blank=True)
    email=models.EmailField(blank=True)
    message=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.email or 'Contact'
