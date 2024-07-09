from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'core/index-2.html')
        else:
            return render(request, 'core/index.html')

        


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
                request.session.set_expiry(0)  # Session expires when the browser is closed
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
        
        return redirect('index')


class Logout(View):
    def get(self, request):
        logout(request)
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
    


class Verification(View):
    def get(self, request):
        return render(request, 'user/verification.html')
    
