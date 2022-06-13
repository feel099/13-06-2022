from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world')

def page(request, pageNum):
    return HttpResponse(f'Страница {pageNum}')