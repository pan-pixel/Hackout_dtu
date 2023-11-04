from django.shortcuts import render, redirect
from time import sleep

# Create your views here.
def home(request):
    # sleep(1)
    if request.method == 'POST':
        company = request.POST['company']
        print(company)
        return redirect('search')
    return render(request,"main.html")


def search(request):
    return render(request,"aftersearch.html")