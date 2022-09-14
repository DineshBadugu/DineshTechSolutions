from django.shortcuts import render,redirect
# from .models import 
# from django.contrib import messages
# from django.contrib.auth.models import User, auth
# from django.core.mail import send_mail

# Create your views here.
def Home(request):
    return render(request,'mainfiles/base.html')
 