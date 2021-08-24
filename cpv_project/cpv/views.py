from django.shortcuts import render
from django.http import HttpResponse

# Home page with search
def index(request):
    return HttpResponse('Page d\'accueil')

# CPV view (with children)
def code(request, cpv_id):
    response = "La page pour le code CPV %s."
    return HttpResponse(response % cpv_id)


