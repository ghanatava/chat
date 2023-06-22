from django.shortcuts import render
from users import forms
from django.contrib import messages
# Create your views here.


def sign_up(request):

    if request.method == 'POST':
        form=forms.UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            message=messages.info(request,'User Registered successfully')
    
    else:
        form=forms.UserRegistrationForm()

    return render(request,'users/sign_up.html',{
            'form':form,
            'message':message
        })





def login(request):
    pass