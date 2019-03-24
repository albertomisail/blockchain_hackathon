from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm, CheckupForm
from .models import Client, Person

def home(request):
    form = LoginForm()
    return render(request, 'health/login.html', {'form': form})

def login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        client_id = form.cleaned_data.get('client_id')
        password = form.cleaned_data.get('password')
        return dashboard(request, client_id)
    return home(request)

def dashboard(request, client_id):
    print(Client.objects.get(person=client_id))
    return render(request, 'health/dashboard.html', {'client': Client.objects.get(person=client_id), 'client_id': client_id})

def checkup(request, client_id):
    if request.method == 'POST':
        form = CheckupForm(request.POST)
        if form.is_valid():
            return HttpResponse('yay')
    else:
        form = CheckupForm()
    return render(request, 'health/checkup.html', {'form': form, 'client_id': client_id})

# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import LoginForm, CheckupForm
# from .models import Client
#
# # Create your views here.
# from django.http import HttpResponse
#
# def home(request):
#     form = LoginForm()
#     return render(request, 'health/login.html', {'form': form})
#
# def login(request):
#     if request.method == 'POST':
#         print('here3')
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             print('here2')
#             client_id = form.cleaned_data.get('client_id')
#             password = form.cleaned_data.get('password')
#             print(client_id)
#             print(password)
#             return redirect('dashboard/'+str(id))
#     else:
#         form = LoginForm()
#         return render(request, 'health/login.html', {'form': form})
#
# def dashboard(request, client_id):
#     return render(request, 'health/dashboard.html', {'client': Client.object.get(pk=client_id), 'client_id': client_id})
#
# def checkup(request, client_id):
#     if request.method == 'POST':
#         form = CheckupForm(request.POST)
#         if form.is_valid():
#             return redirect('dashboard/'+str(client_id))
#     else:
#         form = CheckupForm()
#     return render(request, 'health/checkup.html', {'form': form, 'client_id': client_id})
#
# def payment(request, client_id):
#     return render(request, 'health/payment.html', {'client_id': client_id})
