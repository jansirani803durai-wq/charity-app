# Generated for HopeHands project
from django.db import migrations, models
class Migration(migrations.Migration):
    initial=True
    dependencies=[]
    operations=[
        migrations.CreateModel(name='ContactMessage', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('name', models.CharField(blank=True, max_length=120)),('email', models.EmailField(blank=True, max_length=254)),('message', models.TextField(blank=True)),('created_at', models.DateTimeField(auto_now_add=True))]),
        migrations.CreateModel(name='Donation', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('name', models.CharField(max_length=120)),('email', models.EmailField(max_length=254)),('address', models.TextField()),('amount', models.CharField(max_length=30)),('custom_amount', models.PositiveIntegerField(blank=True, null=True)),('cause', models.CharField(max_length=120)),('created_at', models.DateTimeField(auto_now_add=True))]),
        migrations.CreateModel(name='Volunteer', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('full_name', models.CharField(max_length=120)),('email', models.EmailField(max_length=254)),('phone', models.CharField(max_length=15)),('interest', models.CharField(max_length=100)),('availability', models.CharField(max_length=100)),('created_at', models.DateTimeField(auto_now_add=True))]),
    ]
