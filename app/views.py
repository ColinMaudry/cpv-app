from django.http import HttpResponse, Http404
from django.apps import apps
from django.template import loader
from django.shortcuts import render
from api.models import Code

# Home page with search
def index(request):
    cpvs = Code.objects.order_by('id')[:5]
    context = { 'cpvs': cpvs }
    return render(request, 'index.html', context)

# CPV view (with children)
def code(request, cpv_id):
    response = "La page pour le code CPV %s."
    return HttpResponse(response % cpv_id)


# TODO: d'habitude j'ai l'habitude d'utiliser une API pour alimenter une vue HTML. En python je fais reposer les vues
#  HTML sur l'API ?
