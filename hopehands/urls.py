from django.contrib import admin
from django.urls import path
from foundation import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('causes/', views.causes, name='causes'),
    path('donate/', views.donate, name='donate'),
    path('donate/<slug:cause>/', views.donate, name='donate_cause'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('contact/', views.contact, name='contact'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
