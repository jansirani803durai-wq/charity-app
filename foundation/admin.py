from django.contrib import admin
from .models import Donation, Volunteer, ContactMessage
admin.site.register(Donation)
admin.site.register(Volunteer)
admin.site.register(ContactMessage)
