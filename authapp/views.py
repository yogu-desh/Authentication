from django.shortcuts import render
from django.http import HttpResponseRedirect
from authapp.forms import SignUpForm

from django.contrib.auth.decorators import login_required 

# Create your views here.
def home_page_view(request):
    return render(request,'home.html')

# @login_required 
def java_exams_view(request): 
    return render(request,'javaexam.html') 
    
@login_required 
def python_exams_view(request): 
    return render(request,'pythonexam.html') 
    
@login_required 
def aptitude_exams_view(request): 
    return render(request,'aptitudeexams.html') 
    
def logout_view(request): 
    return render(request,'logout.html')

def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'signup.html', {'form': form})

