from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import Contactform

# Create your views here.
def home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "GET":
        form = Contactform()
    else:
        form = Contactform(request.POST)
        if form.is_valid():
            
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            try:
                send_mail( subject, message, from_email, ["admin@example.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "contact.html", {"form": form})

def successView(request):
    return HttpResponse("Success! Thank you for your message.")
def success(request):
    return HttpResponse('Success!! Thank you for your message! I will get back to you soon. \n Have a good day! 😊')