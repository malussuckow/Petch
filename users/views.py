from django.shortcuts import render,redirect
from users.forms import registerUserForms,loginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def registerUsers(request):
    
    if request.method == 'POST':
        form=registerUserForms(request.POST,request.FILES)
        if form.is_valid():
            usuario=form.save(commit=False)

            usuario.set_password(
                form.cleaned_data['password']
            )
            usuario.save()

            return redirect('login')
    else:
        form=registerUserForms()

    return render(request,'users.html',{'form': form})

def loginUser(request):
    if request.method == 'POST':
        form=loginForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data['password']
            username=form.cleaned_data['username']

            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                if user.user_type == 'TUTOR':
                    return redirect('dashboardTutor')
                elif user.user_type == 'ONG':
                    return redirect('dashboardOng')
            else:
                messages.error(request,"Usuario ou senha inválidos")
                
    else:
        form=loginForm()
            
    return render(request,'login.html',{'form': form})