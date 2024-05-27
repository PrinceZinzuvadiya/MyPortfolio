from django.shortcuts import render, redirect
from .forms import contact_form
from .models import contactmodel
from django.contrib import messages
from django.core.mail import send_mail

def home(request):
    return render (request, 'home.html')

def contact(request):
    if request.method == 'POST':
        messageform = contact_form(request.POST)
        if messageform.is_valid():
            message = messageform.save(commit=False)
            email = message.email
            
            send_mail(
                    subject="Thank you for contacting me!!!",
                    message=f"Dear User,\n\nI appreciate your interest. Stay connected. \n\nThanks & Regards \nPrince | Python Developer \n+91 635 261 3163 | pazinzuvadiya@gmail.com",
                    from_email='pazinzuvadiya@gmail.com',
                    recipient_list=[email],
                )
            messageform.save()
            return redirect ('thankyou')
        else:
            messages.error (request, "Something went wrong. Please try again.")
    return render (request, 'contact.html')

def thankyou(request):
    return render (request, 'thankyou.html')