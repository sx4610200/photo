from django.shortcuts import render
# Create your views here.
def novel(request):

    return render(request, 'index.html')