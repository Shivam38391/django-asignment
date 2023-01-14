from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.shortcuts import redirect 
from django.contrib import messages
from django.contrib.auth import authenticate  , login
# Create your views here.

def index(request):
    return render(request,'acounts/index.html')

def register(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            
            messages.success(request, f'welcome {username} your account is created')
            
            return redirect('login_view')
    else:
        form = RegisterForm()
    context = {
        "form": form,
    }
    return render(request, "acounts/register.html", context )




def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None and user.is_doctor:
                login(request, user)
                return redirect('doctorpage')
            elif user is not None and user.is_patient:
                login(request, user)
                return redirect('patientpage')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'acounts/login.html', {'form': form, 'msg': msg})
        
        
def doctor(request):
    return render(request,'acounts/doctor.html')


def patient(request):
    return render(request,'acounts/patient.html')


