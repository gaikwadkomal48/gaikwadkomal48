
from django.shortcuts import render,redirect
from django.core.mail import BadHeaderError, send_mail

from websiteapp.forms import contactUs
from django.conf import settings as config
from django.conf import settings as conf_set
from socket import gaierror
from django.contrib import messages
from smtplib import SMTPAuthenticationError, SMTPDataError
from websiteapp.models import carousel,features,clients,aboutus
 


cname=config.CNAME

# Create your views here.

def contact_us(request):
    if request.method == 'GET':
        form = contactUs()
    else:
        form = contactUs(request.POST)
        if form.is_valid():
            person_name=form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            user_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            message_send="\n Name : "+person_name+"\n Message : "+message+"\n User Email : "+user_email
            from_email=conf_set.EMAIL_HOST_USER
            try:
                send_mail(subject,message_send,from_email, ['gaikwadkomal48@gmail.com'])
            except (BadHeaderError,gaierror,SMTPAuthenticationError,SMTPDataError):
                messages.error(request,"Check your Internet connection... Try again")
                return redirect('contactpage')
            messages.success(request,"Thank you for contacting! Your form successfully submited")
            return redirect('contactpage')
            
    context = {
        'form': form,
        
    }        
    return render(request, "webpages/contactus.html",context)









def websiteapp_homepage(request):
    car=carousel.objects.all()
    ab=aboutus.objects.all()
    f=features.objects.all()
    c=clients.objects.all()



    page_title="Bodhi Technology"
    text="this my home page"
    choose="Why you choose-Us?"
    # about="About Us"
    client="Our Clients"

    context={
        'car':car,
        'f':f,
        'c':c,
        'ab':ab,

    'title':page_title,
    'text':text,
    'client':client,
    'choose':choose,
    # 'about':about,
    'cname':cname
    
    }
    return render(request,'webpages/index.html',context)

def homepage(request):
    return render(request,"layout/weblayout.html")