from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.conf import settings
import requests,string,random,smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.contrib.auth.models import User
from .models import Temp_user
from datetime import datetime
from django.contrib.auth.hashers import make_password

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def check_captcha(r):
    params = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': r.POST.get('g-recaptcha-response'),
            'remoteip': get_client_ip(r)
        }
    rs=requests.get("https://www.google.com/recaptcha/api/siteverify",params=params,verify=True)
    return rs.json()['success']


def random_string(n):
    res = ''.join(random.choices(string.ascii_letters + string.digits, k = n)) 
    return res


def email_confirmation(email,code,request):
    path=request.build_absolute_uri()
    message = MIMEMultipart("alternative")
    message["Subject"] = "Email Confirmation"
    message["From"] = 'registeration@ahjafar.ir'
    message["To"] = email
    text = "برای فعالسازی ایمیل خود روی پیوند زیر کلیک کنید"
    text=text+"\n \
                {}?email={}&code={}".format(path,email,code)
    message.attach(MIMEText(text, "plain"))
    context = ssl.create_default_context()
    s = smtplib.SMTP_SSL('mail.ahjafar.ir',465,context=context)
    s.login('registeration@ahjafar.ir','ahjafar81')
    s.sendmail('registeration@ahjafar.ir',email, message.as_string())
    s.quit()
    #return render(request, 'email_confirmation.html')



def register(request):
    if request.method == "POST":
        form = NewUserForm()
        if check_captcha(request):
            if User.objects.filter(username=request.POST['username']).exists():
                return render(request, 'registeration.html', {'form': form,'udisplay':'block','site_key':settings.RECAPTCHA_SITE_KEY})
            if User.objects.filter(email=request.POST['email']).exists():
                return render(request, 'registeration.html', {'form': form,'edisplay':'block','site_key':settings.RECAPTCHA_SITE_KEY})
            else:
                code = random_string(48)
                now = datetime.now().date()
                email = request.POST['email']
                password = make_password(request.POST['password'])
                username = request.POST['username']
                temporarycode = Temp_user(
                email=email, request_date=now, code=code, username=username, password=password)
                temporarycode.save()    
                email_confirmation(email,code,request)
            return render(request, 'email_confirmation.html')
        else:
            return render(request, 'registeration.html', {'form': form,'cdisplay':'block','site_key':settings.RECAPTCHA_SITE_KEY})
    elif 'code' in request.GET:
        code = request.GET['code']
        if Temp_user.objects.filter(code=code).exists():
            new_temp_user = Temp_user.objects.get(code=code)
            newuser = User.objects.create(username=new_temp_user.username, password=new_temp_user.password,
                                          email=new_temp_user.email)
            Temp_user.objects.filter(code=code).delete()
            path=request.build_absolute_uri('/register/')[:-10]+'/login/'
            return render(request,'user_creation.html',{'path':path})
        else:
            return render(request,'user_creation.html',{'display1':'none','display2':'1'})
    else:
        form = NewUserForm()
        return render(request, 'registeration.html', {'form': form,'site_key':settings.RECAPTCHA_SITE_KEY})
