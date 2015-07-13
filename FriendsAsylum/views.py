from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from models import Glossary


def entry(request):
	glossary_list = Glossary.objects.all()
	context_dict = {'glossaries': glossary_list}
	return render(request, 'glossary.html', context_dict)

def index(request):
	return HttpResponse("hello world, youre at the polls index")


class Home(TemplateView):
	template_name = 'index.html'


   

