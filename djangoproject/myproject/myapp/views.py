from django.shortcuts import render

def homepage(request):
    return render(request, "myapp/homepage.html")

def todolist(request):
    return render(request, "myapp/todolist.html")

def about(request):
    return render(request, "myapp/about.html")

def contact(request):
    return render(request, "myapp/contact.html")