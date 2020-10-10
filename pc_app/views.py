from django.shortcuts import render

def index(request):
    return render(request, 'pc_app/index.html')
