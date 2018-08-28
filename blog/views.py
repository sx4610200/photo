from django.shortcuts import render
# Create your views here.
def novel(request):
    print("主页里的session")

    return render(request, 'index.html')