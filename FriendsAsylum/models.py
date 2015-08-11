from django.db import models

class Person(models.Model):
	first_name = models.CharField("First Name", max_length=100)
	last_name = models.CharField("Last Name", max_length=100)
	alias = models.CharField("Alias Name", max_length = 100, blank = True, null = True) #only needed for patients
	birth = models.CharField("Birth Date", max_length=20, blank = True)
	death =  models.CharField("Death Date", max_length=20, blank = True)
	gender =  models.CharField("Gender", blank = True, null = True,  max_length=20)
	birthplace = models.ForeignKey("Place", blank = True, null = True, related_name = "birth_place")	
	role = models.ForeignKey("RoleType", blank = True, null = True, related_name = '%(class)s_Role_1' )
	role2 = models.ForeignKey("RoleType", blank = True, null = True, related_name = '%(class)s_Role_2')
	role3 = models.ForeignKey("RoleType", blank = True, null = True, related_name = '%(class)s_Role_3')

	def __unicode__(self):
		return self.first_name + " " + self.last_name  + " " + self.alias + " " + self.birth +  " " + self.death + " " + self.gender + " " + unicode(self.birthplace) + " " + unicode(self.role) + " " + unicode(self.role2) + " " + unicode(self.role3)          




class Relationship(models.Model):
	person1 = models.ForeignKey("Person", related_name = '%(class)s_Person_1')
	relationship = models.ForeignKey("RelationshipType", blank = True, null = True)
	person2 = models.ForeignKey("Person", related_name = '%(class)s_Person_2')

	def __unicode__(self):
		return unicode(self.person1) + " " + unicode(self.relationship) + " " + unicode(self.person2)

class RelationshipType(models.Model):
	relationship_Type = models.CharField("Relationship Type", max_length = 50, null = True, blank = True)
	description = models.TextField("Description (if necessary)", null = True, blank = True)

	class Meta:
		verbose_name_plural = "Relationship Types"
	
	def __unicode__(self):
		return self.relationship_Type + " " + self.description

class PatientEntry(models.Model):
	patient_Info = models.ForeignKey("Person", null = True)
	admitdate = models.CharField("Entry Date", max_length = 15, blank = True)
	exitdate = models.CharField("Departure Date", max_length = 15, blank = True) 
	status = models.TextField("Status on Discharge", blank=True)
	weekly_Rate = models.CharField("Weekly Rate", max_length = 75, blank = True, null = True)
	notes = models.TextField("Note Field", blank = True, null = True)
	age = models.CharField("Age at Admittance", default = '', max_length = 3, null = True, blank = True)	
	
	class Meta:
		verbose_name_plural = "Patient Entries"	


	def __unicode__(self):
		return unicode(self.patient_Info) +  " " +  self.admitdate + " " + self.exitdate + " " + self.status + " " +  self.weekly_Rate + " " + self.notes + " " + self.age

class Biography(models.Model):
	person_Info = models.ForeignKey("Person")
	biography = models.TextField("Bio")
	
	class Meta:
       		verbose_name_plural = "biographies"
	
	def __unicode__(self): 
		return unicode(self.person_Info) + " " + self.biography



class Place(models.Model):
	name = models.CharField("Name of Place", max_length = 100, blank = True, null = True)
	original_Address = models.CharField("Original Address Place", max_length = 150, blank = True, null = True)
	current_Address = models.CharField("Current Address Place", max_length = 150, blank = True, null = True)
	state = models.CharField("State", max_length = 20, blank = True, null = True)
	country = models.CharField("Country", max_length = 20, blank = True, null = True)
	continent = models.CharField("Continent", max_length = 15, blank = True, null = True)
	description = models.TextField("Description Field", blank = True, null = True)
	place_Type = models.ForeignKey("PlaceType", blank = True, null = True)

	def __unicode__(self):
		return self.name + " " + self.original_Address + " " + self.current_Address + " " + self.state + " " + self.country + " " + self.continent + " " + " " + self.description + " " + unicode(self.place_Type)

class PlaceType(models.Model):
	place_Type = models.CharField("Place Type", max_length = 50, null = True, blank = True)
	description = models.TextField("Place Description", blank = True, null = True)

	class Meta:
       		verbose_name_plural = "Place Types"


	
	def __unicode__(self):
		return self.place_Type + " " + self.description
		
class GeoPlace(models.Model):
	latitude = models.FloatField(null = True)
	longitude = models.FloatField(null = True)
	place_Info = models.ForeignKey("Place", blank = True, null = True)


	def __unicode__(self):
		return unicode(self.latitude) + " " + unicode(self.longitude) + " " + unicode(self.place_Info)

class MeetingtoPersonRelationship(models.Model):
	meeting = models.ForeignKey("Meeting")
	date_Attended = models.CharField("Date of Attendance", max_length = 15, null = True, blank = True)
	person = models.ForeignKey("Person")

	class Meta:
       		verbose_name_plural = "Meeting to Person Relationships"

	def __unicode__(self):
		return unicode(self.meeting) + " " + self.date_Attended + " " + unicode(self.person) 

class Meeting(models.Model):
	meeting_Info = models.ForeignKey("Place")
	meeting_Type = models.ForeignKey("MeetingType", null = True, blank = True)

	def __unicode__(self):
		return unicode(self.meeting_Info) + " " + unicode(self.meeting_Type) 

class MeetingType(models.Model):
	meeting_Type = models.CharField("Meeting Type", max_length = 75)
	description =  models.TextField("Description of Meeting", null = True, blank = True)
	class Meta:
       		verbose_name_plural = "Meeting Types"

	def __unicode__(self): 
		return self.meeting_Type + " " + self.description

class Residence(models.Model):
	residence = models.ForeignKey("Place")
	date_Lived_There = models.CharField("Date of Residence", max_length = 15, null = True, blank = True)
	person = models.ForeignKey("Person")
	
	def __unicode__(self):
		return unicode(self.residence) + " " + self.date_Lived_There + " " + unicode(self.person)

class RoleType(models.Model):
	role = models.CharField("Role_Type", max_length = 50, blank = True, null = True)
	description = models.TextField("Description of Role", blank = True, null = True)
	class Meta:
       		verbose_name_plural = "Role Types"


	
	def __unicode__(self):
		return self.role + " " + self.description

class Glossary(models.Model):
	word = models.CharField("Word", max_length = 100, blank = True, null = True)
	definition = models.TextField("Definition of Word", null = True, blank = True)
	
	class Meta:
		verbose_name_plural = "Glossary"
	
	def __unicode__(self):
		return self.word + " " + self.definition

class Text(models.Model):
	name = models.CharField("Name of Text", max_length = 150, blank = True)
	volume = models.CharField("Vol. #", max_length = 4, blank = True, null = True)
	text_Type = models.ForeignKey("Text_Type", null = True, blank = True)
	author = models.ForeignKey("Person", blank = True, null = True, related_name = '%(class)s_Author')
	clerk = models.ForeignKey("Person", blank = True, null = True, related_name = '%(class)s_Clerk')
	dates = models.CharField("Dates of Text", max_length = 40, blank = True, null = True)
	description = models.TextField("Description of Text", blank = True, null = True)
	
	def __unicode__(self):
		return self.name + " " + self.volume + " " + unicode(self.text_Type) + " " + unicode(self.author) + " " + unicode(self.clerk) + " " + self.dates + " " + self.description

class Text_Type(models.Model):
	text_Type = models.CharField("Text Type", max_length = 100, blank = True, null = True)
	description = models.TextField("Description of Text", null = True, blank = True)

	class Meta:
		verbose_name_plural = "Text Types"

	def __unicode__(self):
		return self.text_Type + " " + self.description

class Text_Relationship(models.Model):
	text = models.ForeignKey("Text", null = True, blank = True)
	person1 = models.ForeignKey("Person", null = True, blank = True, related_name = '%(class)s_Person_1')
	person2 = models.ForeignKey("Person", null = True, blank = True, related_name = '%(class)s_Person_2')
	person3 = models.ForeignKey("Person", null = True, blank = True, related_name = '%(class)s_Person_3')
	person4 = models.ForeignKey("Person", null = True, blank = True, related_name = '%(class)s_Person_4')
	person5 = models.ForeignKey("Person", null = True, blank = True, related_name = '%(class)s_Person_5')
	person6 = models.ForeignKey("Person", null = True, blank = True, related_name = '%(class)s_Person_6')
	person7 = models.ForeignKey("Person", null = True, blank = True, related_name = '%(class)s_Person_7')
	person8 = models.ForeignKey("Person", null = True, blank = True, related_name = '%(class)s_Person_8')
	person9 = models.ForeignKey("Person", null = True, blank = True, related_name = '%(class)s_Person_9')
	person10 = models.ForeignKey("Person", null = True, blank = True, related_name = '%(class)s_Person_10')
	person11 = models.ForeignKey("Person", null = True, blank = True, related_name = '%(class)s_Person_11')
	person12 = models.ForeignKey("Person", null = True, blank = True, related_name = '%(class)s_Person_12')
	person13 = models.ForeignKey("Person", null = True, blank = True, related_name = '%(class)s_Person_13')
	person14 = models.ForeignKey("Person", null = True, blank = True, related_name = '%(class)s_Person_14')
	person15 = models.ForeignKey("Person", null = True, blank = True, related_name = '%(class)s_Person_15')

	class Meta:
        	verbose_name_plural = "Text Relationship Types"

	def __unicode(self):
		return unicode(self.text) + " " + unicode(self.person1) + " " + unicode(self.person2) + " " + unicode(self.person3) + " " + unicode(self.person4) + " " + unicode(self.person5) + " " + unicode(self.person6) + " " + unicode(self.person7) + " " + unicode(self.person8) + " " + unicode(self.person9) + " " + unicode(self.person10) + " " + unicode(self.person11) + " " + unicode(self.person12) + " " + unicode(self.person13) + " " + unicode(self.person14) + " " + unicode(self.person15) 
