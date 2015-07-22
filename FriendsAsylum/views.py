from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from models import Glossary
from models import PatientEntry
from models import Person

def glossary(request):
	glossary_list = Glossary.objects.all()
	word_list = [glossary.word for glossary in glossary_list]
	dict_list = [glossary.definition for glossary in glossary_list]
	glossary_list = zip(word_list, dict_list)
	return render(request, 'glossary.html', {'glossaries': glossary_list})


def profiles(request):
	patient_list = PatientEntry.objects.all()
	person_list = patient_list.patient_Info.objects.all()
	first_list = [person.first_name for person in person_list]
	alias_list = [person.alias for person in person_list]
	birth_list = [person.birth for person in person_list]
	person_list = zip(first_list, alias_list, birth_list)
	admit_list = [patient.admitdate for patient in patient_list]
	exit_list = [patient.exitdate for patient in patient_list]
	stat_list = [patient.status for patient in patient_list]
	rate_list = [patient.weekly_Rate for patient in patient_list]
	note_list = [patient.notes for patient in patient_list]
	age_list = [patient.age for patient in patient_list]
	patient_list = zip(person_list, admit_list, exit_list, stat_list, rate_list, note_list, age_list)
	return render(request, 'patient.html', {'patients': patient_list})


def arch(request):
	return render(request, 'FriendsARCH2.html')

def foundation(request):
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

def index(request):
	return HttpResponse("hello world, youre at the polls index")


class Home(TemplateView):
	template_name = 'index.html'


   

