from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "core/index.html")


def about(request):
    return render(request, "core/about.html")


def contacts(request):
    return render(request, "core/contacts.html")
