from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboardTutor(request):
    return render(request,'tutor/dashboardTutor.html')

@login_required
def dashboardOng(request):
    return render(request,'ong/dashboardOng.html')
# Create your views here.

