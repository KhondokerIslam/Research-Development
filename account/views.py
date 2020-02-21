from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from inputs.models import Input

def signup(request, backend='django.contrib.auth.backends.ModelBackend'):
    if request.method == 'POST':
        #Sign him up
        random_text = Input.objects.order_by('?')[0]
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST.get('username'))
                return render(request,'account/register.html',{'error': 'Username already taken!'} )
            except User.DoesNotExist:
                try:
                    user = User.objects.get(email=request.POST.get('email'))
                    return render(request,'account/register.html',{'error': 'Email already taken!'} )
                except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['username'],request.POST['email'], password = request.POST['password1'],first_name = request.POST['firstname'],last_name = request.POST['lastname']  )
                    auth.login(request,user, backend='django.contrib.auth.backends.ModelBackend')
                    return render(request, 'index.html', {'texts':random_text})
        else:
            return render(request, 'account/register.html', {'error': 'Password Does not match!'} )
    else:
        return render(request, 'account/register.html' )

def user_login(request):
    if request.method == 'POST':
        random_text = Input.objects.order_by('?')[0]
        user =  auth.authenticate(username=request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request,user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'index.html', {'texts':random_text})
        else:
            return render(request,'index.html', {'error': 'Username or Password Does not match!'} )

def user_logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
