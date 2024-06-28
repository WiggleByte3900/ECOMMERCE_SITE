from django.shortcuts import render
from django.http import HttpResponse

def INDEX(request):
    return render(request , 'BLOG/INDEX.HTML')
