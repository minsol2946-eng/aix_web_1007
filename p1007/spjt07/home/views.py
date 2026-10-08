from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# 메인페이지
def index(request):
    return render(request,'index.html')