from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
import redis

# Create your views here.
r = redis.Redis(host= '127.0.0.1', port = 6379, db=1)

def w3school (request):
    return render (request, 'core/w3school.html') 

#logout view
def logout_view (request):
    logout(request)
    return redirect ('w3school')

#login view
def admin_log(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  #authenticating the user
        if user is not None : 
            if user.is_staff: #checking if the user is staff
                login(request, user) 
                admin_ip = request.META.get('REMOTE_ADDR') #getting the first IP address of the admin
                usern = request.POST.get('username') #getting the username of the admin
                current_ip = request.META.get('REMOTE_ADDR') #getting the current IP address of the admin
                r.set(usern, admin_ip, nx = True) #saving the IP address of the admin
                first_ip = r.get(usern).decode() #getting the IP address of the admin
                current_ip = request.META.get('REMOTE_ADDR') #getting the IP address of the admin
                if first_ip != current_ip: #checking if the IP address matches
                    messages.error(request,'WARNING DIFFERENT IP ADDRESS THAN PREVIOUS ONE')  
                    print('WARNING DIFFERENT IP ADDRESS THAN PREVIOUS ONE')  
                    return redirect('addcertificates')  
                else:
                    messages.success(request, 'Login successful')  
                    print('Login successful') 
                    return redirect('addcertificates')  
            else:
                messages.error(request, 'Unauthorized user')  
                print('Unauthorized user')  
                return redirect('admin_log')  
        else:
            messages.error(request, 'Invalid credentials')  
            return redirect('admin_log')  
    c_messages = messages.get_messages(request)  
    return render (request, 'core/admin_log.html', {'c_messages': c_messages}) 