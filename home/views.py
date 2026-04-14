from django.shortcuts import render

def main_page(request):
    return render(request, 'home/home.html')

def sobre(request):
    return render(request, 'home/sobre.html')

def blog(request):
    return render(request, 'home/blog.html')

def contato(request):
    return render(request, 'home/contato.html')

def agendar_consulta(request):
    return render(request, 'home/agendar_consulta.html')


