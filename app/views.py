from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.apps import apps
from django.template import loader
from django.shortcuts import render, get_list_or_404
from api.models import Code
from django.urls import reverse

# Home page with search
def index(request):
    context = {}
    if request.GET and request.GET['text']:
        search_results = Code.objects.filter(name__search=request.GET['text'])
        context = {'search_results': search_results}
    return render(request, 'index.html', context)

# CPV view (with children)
def code(request, cpv_id):
    response = "La page pour le code CPV %s."
    return HttpResponse(response % cpv_id)


# TODO: d'habitude j'ai l'habitude d'utiliser une API pour alimenter une vue HTML. En python je fais reposer les vues
# HTML sur l'API ?
