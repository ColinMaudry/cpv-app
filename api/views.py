from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Code

# Home page with search
def index(request):
    return HttpResponse('Welcome to the API!')

# CPV view (with children)
def code(request, cpv_id: str):
    print(cpv_id)
    cpv = get_object_or_404(Code, pk = cpv_id)
    print(f'id : {cpv.id}, name : {cpv.name}')
    return HttpResponse(f'id : {cpv.id}, name : {cpv.name}')


# TODO: d'habitude j'ai l'habitude d'utiliser une API pour alimenter une vue HTML. En python je fais reposer les vues
#  HTML sur l'API ?
