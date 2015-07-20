from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from models import Glossary
from models import PatientEntry

def glossary(request):
	glossary_list = Glossary.objects.all()
	word_list = [glossary.word for glossary in glossary_list]
	dict_list = [glossary.definition for glossary in glossary_list]
	glossary_list = zip(word_list, dict_list)
	return render(request, 'glossary.html', {'glossaries': glossary_list})


def patient(request):
	patient_list = PatientEntry.objects.all()
	personi_list = [patient.patient_Info for patient in patient_list]
	admit_list = [patient.admitdate for patient in patient_list]
	exit_list = [patient.exitdate for patient in patient_list]
	stat_list = [patient.status for patient in patient_list]
	rate_list = [patient.weekly_Rate for patient in patient_list]
	note_list = [patient.notes for patient in patient_list]
	age_list = [patient.age for patient in patient_list]
	patient_list = zip(personi_list, admit_list, exit_list, stat_list, rate_list, note_list, age_list)
	return render(request, 'patient.html', {'patients': patient_list})


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


   

