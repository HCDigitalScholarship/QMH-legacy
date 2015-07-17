from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from models import Glossary


def glossary(request):
	glossary_list = Glossary.objects.all()
	word_list = [glossary.word for glossary in glossary_list]
	dict_list = [glossary.definition for glossary in glossary_list]
	glossary_list = zip(word_list, dict_list)
	return render(request, 'glossary.html', {'glossaries': glossary_list})

def arch(request):
	return render(request, 'FriendsARCH.html')

def foundation(request):
	return render(request, 'FriendsFOUND.html')

def struct(request):
	return render(request, 'FriendsGOV.html')

def profiles(request):
	return render(request, 'FriendsPRO.html')


def index(request):
	return HttpResponse("hello world, youre at the polls index")


class Home(TemplateView):
	template_name = 'index.html'


   

