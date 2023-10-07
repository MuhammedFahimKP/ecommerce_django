from django.shortcuts import render,redirect
from django.views import View
from .models import MyUser
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage



#creat your view
class SignupView(View):
  
    def get(self,request):
        
        if request.user.is_authenticated:
            return redirect('home')
         
        return render(request,'log/signup.html')

    def post(self,request):

        context={
            'error':None,
            'res':None
        }

        email = request.POST.get('email')
        if  MyUser.objects.filter(email=email).exists():
            context['error'] = 'you already have an accout'
        else:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            pass2 = request.POST.get('pass2')
            password = make_password(pass2)
              
            user  = MyUser.objects.create(email=email,first_name=fname,last_name=lname,password=password)
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate Your Account'
            message      = render_to_string('log/activation.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.id)),
                'token':default_token_generator.make_token(user),

            })

            to_email = email
            sendemail = EmailMessage(mail_subject,message,to=[to_email]) 
            sendemail.send()
            context['res'] = 'sucess account created'
            email = None
            

        return render(request,'log/signup.html',context)
    
    



class Activation(View):

    def get(self,request,uidb64,token):

        try:
            uid = urlsafe_base64_decode(uidb64).decode()

            user = MyUser._default_manager.get(pk=uid)

        except(TypeError,ValueError,OverflowError,MyUser.DoesNotExist):
            user = None
        
        print(user)
        print(token)
        
        if user is not None and default_token_generator.check_token(user, token):
            
            user.is_active = True
            user.save()
            messages.success(request,'Your account is activated now you can login')
            return redirect('signin') 
        
        else:
            messages.error(request,'Your  Token is not valid ')
            return redirect('signin')
        
        return redirect('signin')
        





class SigninView(View):

    def get(self,request):
        
        if request.user.is_authenticated:
            return redirect('home')
        
        return render(request,'log/signin.html')
    
    def post(self,request):

        context = {

            'error':None
        }
        
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        print(email)
        print(pass1)

        try :  
            user = auth.authenticate(email=email ,password = pass1)
            auth.login(request,user)
            return redirect('home')

        except:
            context['error'] = "Wrong password or Email"
            
        return render(request,'log/signin.html',context)