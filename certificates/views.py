from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .forms import NewCertificates
from django.contrib.auth.models import User
from .models import Certificates,SetCertificates
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='admin_log')
@staff_member_required
def addcertificates(request):
    certificates = Certificates.objects.all()
    if request.method == 'POST':
        form = NewCertificates(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Certificate added successfully')
            return redirect('addcertificates')
        messages.error(request, 'Error! Please check your data.')
    else:
        form = NewCertificates()
    c_messages = messages.get_messages(request)
    return render(request, 'certificates/addcertificates.html', {'form': form, 'c_messages' : c_messages, 'certificates': certificates})

@login_required(login_url='admin_log')
@staff_member_required
def set_certificates(request):
    students = User.objects.all() 
    certificates = Certificates.objects.all()
    if request.method == 'POST':
        try:
            username = request.POST.get('username') #Gets the value from the username field
            name_certificate = request.POST.get('name_certificate') #Gets the value from the name_certificate field
            vote = request.POST.get('vote') #Gets the value from the vote field
            student = User.objects.get(username=username) 
            certificate = Certificates.objects.get(name_certificate=name_certificate)
            new_certificate = SetCertificates(students=student, certificates=certificate,vote = vote) #Creates a new certificate object
            new_certificate.save() #Saves the new certificate object
            messages.success(request, 'Certificate assigned successfully.')
            return redirect ('certificates')
        except ValueError:
            messages.error(request, 'Please check your transactions or settings.')
        except Exception: 
            messages.error(request, 'An error occurred') 
    c_messages = messages.get_messages(request)
    return render(request, 'certificates/set_certificates.html', {'students': students, 'certificates' : certificates, 'c_messages' : c_messages})

def search_certificates(request):
    #Get all certificates
    certificates = SetCertificates.objects.all() 
    code = None
    if request.method == 'GET': 
        q_code = request.GET.get('code') #Gets the value from the code field
        if q_code:
            code = SetCertificates.objects.filter(certificates__code=q_code) #Filter certificates by code field
            if not code:  
                messages.error(request, 'Certificate not found') # This line sets an error message if the code is not found
    c_messages = messages.get_messages(request) # This line gets all the messages
    return render (request, 'certificates/search_certificates.html', {'code' : code, 'certificates' : certificates, 'c_messages': c_messages})