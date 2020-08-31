from django.shortcuts import render,redirect
from .forms import NewUserForm,ResetPasswordForm1,ResetPasswordForm2,LoginForm
from django.conf import settings
import requests,string,random,smtplib,ssl,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Temp_user,Password_reset
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from web.models import Balance

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


def email_sender(email,code,request,mode):
    path=request.build_absolute_uri()
    message = MIMEMultipart("alternative")
    if mode==1:
        message["Subject"] = "Email Confirmation"
        text = "برای فعالسازی اکانت خود روی پیوند زیر کلیک کنید"
        text=text+"\n {}?email={}&code={}".format(path,email,code)
    else:
        message["Subject"] = "Password Reset"
        text = "برای بازیابی پسورد خود روی پیوند زیر کلیک کنید"
        text=text+"\n {}?email={}&code={}".format(path,email,code)
    message["From"] = 'registeration@ahjafar.ir'
    message["To"] = email
    message.attach(MIMEText(text, "plain"))
    
    context = ssl.create_default_context()
    s = smtplib.SMTP_SSL('mail.ahjafar.ir',465,context=context)
    s.login('registeration@ahjafar.ir','ahjafar81')
    s.sendmail('registeration@ahjafar.ir',email, message.as_string())
    s.quit()


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
                temporarycode = Temp_user(email=email, request_date=now, code=code, username=username, password=password)
                temporarycode.save()    
                email_sender(email,code,request,1)
                context={'message':'<br><h1 class=""> ثبت نام شما با موفقیت انجام شد </h1><br> از اینکه در سایت ما ثبت نام کرده اید از شما سپاسگزاریم <br> برای فعالسازی حساب کاربری لطفا ایمیل ارسال شده را تایید کنید <br>',
                         'title':'تایید ایمیل'}
                return render(request, 'message.html',context)
        else:
            return render(request, 'registeration.html', {'form': form,'cdisplay':'block','site_key':settings.RECAPTCHA_SITE_KEY})
    elif 'code' in request.GET:
        code = request.GET['code']
        if Temp_user.objects.filter(code=code).exists():
            new_temp_user = Temp_user.objects.get(code=code)
            User.objects.create(username=new_temp_user.username, password=new_temp_user.password,
                                          email=new_temp_user.email)
            Temp_user.objects.filter(code=code).delete()
            path=request.build_absolute_uri('/register/')[:-10]+'/login/'
            context={'message':'<br><h1 class=""> حساب کاربری شما با موفقیت فعال شد. </h1><br> شما می توانید از  <br> <a href="{}"> اینجا </a> وارد حساب خود شوید. <br>'.format(path),
                     'title':'اکانت فعال شد'}
            return render(request,'message.html',context)
        else:
            context={'message':' <br><h1 class=""> این کد فعالسازی معتبر نیست. در صورت نیاز دوباره تلاش کنید. <br>',
                     'title':'فعالسازی ناموفق'}
            return render(request,'message.html',{'display1':'none','display2':'1'})
    else:
        form = NewUserForm()
        context={}
        context['form']=form
        context['site_key']=settings.RECAPTCHA_SITE_KEY
        return render(request, 'registeration.html', context)


def reset_pasword(request):

    if 'email' in request.POST:
        if check_captcha(request):
            email=request.POST['email']
            if not User.objects.filter(email=email).exists():
                form =ResetPasswordForm1()
                context={}
                context['form']=form
                context['site_key']=settings.RECAPTCHA_SITE_KEY
                context['edisplay']='block'
                context['path']=request.build_absolute_uri('/resetpassword/')[:-15]+'/register/'
                return render(request, 'resetpassword1.html', context)
            else:
                code=random_string(48)
                date=datetime.now().date()
                Password_reset.objects.create(code=code,request_date=date,email=email)
                email_sender(email,code,request,2)
                context={'message':'<br><h1> لینک باز نشانی رمز به ایمیل شما ارسال شد</h1><br>',
                         'title':'بازنشانی رمز عبور'}
                return render(request, 'message.html',context)
        else:
            form =ResetPasswordForm1()
            context={}
            context['form']=form
            context['site_key']=settings.RECAPTCHA_SITE_KEY
            context['cdisplay']='block'
            return render(request,'resetpassword1.html',context)
    if 'password' in request.POST:
        if Password_reset.objects.filter(Is_ok=True).exists():
            new_temp_user=Password_reset.objects.get(Is_ok=True) 
            this_user=User.objects.get(email=new_temp_user.email)
            this_user.set_password(request.POST['password'])
            this_user.save()
            Password_reset.objects.filter(Is_ok=True).delete()  
            path=request.build_absolute_uri('/resetpassword/')[:-15]+'/login/'
            context={'message':'<br><h1 class=""> رمز عبور شما با موفقیت تغییر کرد. </h1>نام کاربری شما:{}<br><br> شما می توانید از  <br> <a href="{}"> اینجا </a> وارد حساب خود شوید. <br>'.format(this_user.username,path),
                    'title':'رمز تغییر کرد'}
            return render(request,'message.html',context)
        else: 
            return render(request,'message.html',{'message':'<h1>خطا</h1>'})
    elif 'code' in request.GET:
        code = request.GET['code']
        if Password_reset.objects.filter(code=code).exists():
            new_temp_user = Password_reset.objects.get(code=code)
            new_temp_user.Is_ok=True
            new_temp_user.save()
            form =ResetPasswordForm2()
            context={}
            context['form']=form
            return render(request,'resetpassword2.html',context)
        else:
            context={'message':' <br><h1 class=""> این کد بازیابی معتبر نیست. در صورت نیاز دوباره تلاش کنید. <br>',
                     'title':'فعالسازی ناموفق'}
            return render(request,'message.html',context)
    else:
        form =ResetPasswordForm1()
        context={}
        context['form']=form
        context['site_key']=settings.RECAPTCHA_SITE_KEY
        return render(request,'resetpassword1.html',context)

def Login(request):
    if 'username' in request.POST:
        if check_captcha(request):
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                #context={'message':username+'   '+ password+'   '+ str(user)}
                #return render(request,'message.html',context)
                if 'next' in request.GET:
                    return redirect('http://localhost:8009{}'.format(request.GET['next']))
                return redirect('http://localhost:8009')
            else:
                form=LoginForm()
                return render(request, 'login.html', {'form': form,'site_key':settings.RECAPTCHA_SITE_KEY,'message' :'نام کاربری یا رمز عبور نادرست است'})
        else:
            form=LoginForm()
            return render(request, 'login.html', {'form': form,'cdisplay':'block','site_key':settings.RECAPTCHA_SITE_KEY})
    elif 'next' in request.GET:
        form=LoginForm()
        return render(request, 'login.html', {'form': form,'site_key':settings.RECAPTCHA_SITE_KEY,'message':'برای دسترسی به این صفحه ابتدا باید وارد شوید.'})
    else:
        context={}
        context['form']=LoginForm()
        context['site_key']=settings.RECAPTCHA_SITE_KEY
        return render(request,'login.html',context)

# @login_required
# def login_check(request):
#     return render(request,'message.html', {'message':'Hi There'})

def Logout(request):
    logout(request)
    return redirect('http://localhost:8009/')

def index(request):
    context={}
    #print(request.user.is_authenticated())
    if request.user.is_authenticated:
        context['balance']='{:,}'.format(Balance.objects.get(user=request.user).amount)+'ريال'
    return render(request,'index.html',context)