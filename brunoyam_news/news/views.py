from django.shortcuts import render
def index(request):
    return render(request,'news/index.html')
def learning(request):
    return render(request, 'news/learning.html')
