from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from models import Glossary
from models import PatientEntry
from models import Person

def glossary(request):
	glossary_list = Glossary.objects.order_by('word')
	word_list = [glossary.word for glossary in glossary_list]
	dict_list = [glossary.definition for glossary in glossary_list]
	glossary_list = zip(word_list, dict_list)
	return render(request, 'glossary.html', {'glossaries': glossary_list})

def ptable(request):
	patient_list = PatientEntry.objects.order_by('patient_Info')
	return render(request, 'table.html', {'patients': patient_list})
	

def profiles(request):
	patient_list = PatientEntry.objects.order_by('patient_Info')
	return render(request, 'patient.html', {'patients': patient_list})

def contrib(request):
	return render(request, 'contrib.html')

def related(request):
	return render(request, 'related.html')

def essay(request):
	return render(request, 'pdf.html')

def features(request):
	return render(request, 'features.html')

def future(request):
	return render(request, 'future.html')

def arch(request):
	return render(request, 'FriendsARCH2.html')

def found(request):
	return render(request, 'FriendsFOUND.html')

def structure(request):
	return render(request, 'FriendsGOV.html')

def religion(request):
	return render(request, 'FriendsREL.html')

def medical(request):
	return render(request, 'FriendsMED.html')

def moral(request):
	return render(request, 'FriendsMORAL.html')

def occu(request):
	return render(request, 'FriendsOCCU.html')

def theology(request):
	return render(request, 'FriendsTHEO.html')

def york(request):
	return render(request, 'FriendsYORK.html')

def bibliography(request):
	return render(request, 'bib.html')

def pieq(request):
	return render(request, 'quakerpiechart.html')

def pieq2(request):
	return render(request, 'quakerpiechartwophilly.html')

def bargraph(request):
	return render(request, 'bargraph.html')

def handler404(request):
	response = render_to_response('detail.html', {}, context_instance = RequestContext(request))
	response.status_code = 404
	return response

class Home(TemplateView):
	template_name = 'index.html'


   

