from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
import random
from . import models


class SignIn(View):
    def get(self, request):
        return redirect('index')
    
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('rememberme', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)
            messages.success(request, 'You\'re successfully logged in!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
        
        return redirect('index')


class Logout(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You\'re successfully logged out')
        return redirect('index')
    
    

class Navigator(View):
    def get(self, request):
        return render(request, 'user/navigator-register.html')
    


class CompanySignUp(View):
    def get(self, request):
        return render(request, 'user/company-signup.html')
    

    def post(self, request):
        name = request.POST.get('name')
        ceo = request.POST.get('ceo')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        print(name, ceo, email, password, confirm_password)
        return redirect('verification')


class FreelancerSignUp(View):
    def get(self, request):
        return render(request, 'user/freelancer-signup.html')
    
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.warning(request, 'Passwords does not match!')
            return redirect('freelancer-signup')
        user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
        # user.is_active = False
        # user.save()
        # code = random.randint(100000, 999999)
        # try:
        #     send_mail(
        #         'Verification Code',
        #         f'Your verification code is: {code}',
        #         settings.EMAIL_HOST_USER,
        #         [email],
        #     )
        # except Exception as e:
        #     messages.error(request, f'Error sending email: {e}')
        #     return redirect('freelancer-signup')
        # verification = models.Verification.objects.create(user=user, code=code)
        # context = {
        #     'user_id': user.id,
        # }
        return redirect('verification')
    


class Verification(View):
    def get(self, request):
        return render(request, 'user/verification.html')