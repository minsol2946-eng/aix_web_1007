from django.shortcuts import render

# Create your views here.
def swrite(request):
    if request.method=='GET':
        return render(request.swrite.html)
    elif:
        print(request.POST.get('name'))
        print(request.POST.get('major'))
        print(request.POST.get('grade'))
        print(request.POST.get('age'))
        print(request.POST.get('gender'))
        return redirect('/student/slist')
    
def slist(request):
    return render(request.slist.html)