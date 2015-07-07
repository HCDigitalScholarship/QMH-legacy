
m django.http import HttpResponse, HttpResponseNotFound
#from django.template import RequestContext, loader
from django.shortcuts import render
from django.contrib.auth.models import User
#from json import dumps, dump
import ast 
import sys
import re
from models import Person
from models import Biography
from models import Place
from models import PlaceType
from models import Relationship
from models import RelationshipType
from models import PatientEntry
from models import MeetingtoPersonRelationship
from models import Meeting
from models import MeetingType
from models import Residence
from models import RoleType

authenticate = False

def index(request):
	if request.user.is_authenticated() or not authenticate:
	#	return render(request, 'FriendsAsylumHOME.html')
	else:
	#	return HttpResponse('<h1> I\'m sorry, you must be authenticated to view this page </h1> <p> Please login and then try again </p>')

def page(request, page_id):
	if request.user.is_authenticated() or not authenticate:
	#	print page_id
		if page_id == "home":
	#		return render(request, '')
		elif page_id == "":
	#		retrun render(request, '')
		else:
	#		return HttpResponse('<h1> I\'m sorry, you must be authenticated to view this page </h1> <p> Please login and then try again </p>')

def pageRank(request):
	if request.user.is_authenticated() or not authenticate:
	#	return render(request, '')
	else:
	#	return HttpResponse('<h1> I\'m sorry, you must be authenticated to view this page </h1> <p> Please login and then try again </p>')

pageRank_info(request):
	if request.user.is_authenticated() or not authenticate:
	#	return render(request, 'PageRank.html')
	else:
	#	return HttpResponse('<h1> I\'m sorry, you must be authenticated to view this page </h1> <p> Please login and then try again </p>')    

