from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        print("Login!")
        user = auth.authenticate(username='reporter', password=request.POST['password'])
        if user is not None:
            # Success! User Logging in
            auth.login(request, user)
            return redirect('report')
        else:
            return render(request, 'login/login.html', {'error':True, 'login_error':'Incorrect Pin'})
        return render(request, 'reports/report.html')
    return render(request, 'login/login.html')