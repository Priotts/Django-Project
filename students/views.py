from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Student added successfully')
                return redirect('signup')
            except:
                messages.error(request, 'Error! Please check your data.')
                return redirect ('signup')
    else:
        form = SignUpForm()
    c_messages = messages.get_messages(request)
    return render(request, 'students/signup.html', {'form': form, 'c_messages' : c_messages})