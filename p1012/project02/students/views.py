from django.shortcuts import render, redirect
from students.models import Students

def swrite(request):
    if request.method=='GET':
        return render(request,'swrite.html')
    elif request.method=='POST':
        name=request.POST.get('name')
        major=request.POST.get('major')
        age=request.POST.get('age')
        grade=request.POST.get('grade')
        gender=request.POST.get('gender')
        return redirect('/students/slist/')

def slist(request):
    qs=Students.objects.all()
    context={'list':qs}
    return render(request,'slist.html',context)