from django.shortcuts import render
from django.http import HttpResponse
from calc.models import *
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
#for backend operations
def newsletter2(request):
	return render(request,"newsletter.html")
@csrf_exempt
def savedata(request):
    if request.method=='POST':
        n=request.POST.get('name')
        e=request.POST.get('email')
        obj=newsletter1(name=n,email=e)
        obj.save()
        subject = 'welcome to My Project'
        message = f'Hi, Thank you for registering in my project.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]
        send_mail( subject, message, email_from, recipient_list )
        return HttpResponse("Data saved to database")
