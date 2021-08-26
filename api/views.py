from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Code

# Home page with search
def index(request):
    return HttpResponse('Welcome to the API!')

# CPV view (with children)
def code(request, cpv_id: str):
    cpv = Code.objects.filter(id=cpv_id)
    if len(cpv) == 1:
        return HttpResponse(f'id : {cpv.id}, name : {cpv.name}\n')
    else:
        return Http404('Non trouvé')


# TODO: d'habitude j'ai l'habitude d'utiliser une API pour alimenter une vue HTML. En python je fais reposer les vues
#  HTML sur l'API ?
