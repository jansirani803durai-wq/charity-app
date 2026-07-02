from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DonationForm, VolunteerForm

def home(request): return render(request,'page.html',{'page':'home','img':'home.png'})
def about(request): return render(request,'page.html',{'page':'about','img':'about.png'})
def causes(request): return render(request,'page.html',{'page':'causes','img':'causes.png'})
def contact(request): return render(request,'page.html',{'page':'contact','img':'contact.png'})
def thank_you(request): return render(request,'page.html',{'page':'thanks','img':'thanks.png'})
def donate(request, cause=''):
    initial={'cause': cause.replace('-', ' ').title()} if cause else {}
    form=DonationForm(request.POST or None, initial=initial)
    if request.method=='POST' and form.is_valid():
        form.save(); messages.success(request,'Donation saved successfully. Thank you!'); return redirect('thank_you')
    return render(request,'donate.html',{'page':'donate','img':'donate.png','form':form})
def volunteer(request):
    form=VolunteerForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save(); messages.success(request,'Volunteer details saved successfully.'); return redirect('thank_you')
    return render(request,'page.html',{'page':'volunteer','img':'volunteer.png','form':form})
