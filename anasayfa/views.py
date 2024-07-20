from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request,"index.html", {})

def faysal_view(request):
    return render(request, "vlogs/faysal.html", {})


def hakkinda_view(request):
    return render(request, "Hakkinda.html", {})

def toplanti_view(request):
    return render(request, "toplanti.html", {})


def amacimiz_view(request):
    return render(request, 'Amacimiz.html')

def yonetim_view(request):
    return render(request, 'Yonetim.html' )

def iletisim_view(request):
    return render(request, 'iletisim.html')

def bilimkurulu_view(request):
    return render(request, 'bilimkurulu.html' )




