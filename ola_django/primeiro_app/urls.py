from django.urls import path
from django.http import HttpResponse

def oiDjango(request):
    return HttpResponse('Ola primeiroAPP')

urlpatterns = [
     path('ola/', oiDjango),
]
