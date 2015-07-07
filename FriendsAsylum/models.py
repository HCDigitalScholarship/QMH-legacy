
m django.db import models

class Person(models.Model):
	first_name = models.CharField("First Name", max_length=100)
	last_name = models.CharField("Last Name", max_length=100)
	alias = models.CharField("Alias Name", max_length = 100, blank = True, null = True) #only needed for patients
	birth = models.CharField("Birth Date", max_length=20, blank = True)
	death =  models.CharField("Death Date", max_length=20, blank = True)
	gender =  models.CharField("Gender", blank = True, null = True,  max_length=20)
	birthplace = models.ForeignKey("Place", blank = True, null = True, related_name = "Place of Birth")	
	role = models.ForeignKey("RoleType", blank = True, null = True, related_name = "Role Type1")
	role2 = models.ForeignKey("RoleType", blank = True, null = True, related_name = "Role Type2")
	role3 = models.ForeignKey("RoleType", blank = True, null = True, related_name = "Role Type3")

	def __unicode__(self):
		return self.first_name + " " + self.last_name  + " " + self.alias + " " + self.birth +  " " + self.death + " " + self.gender + " " + unicode(self.birthplace) + " " + unicode(self.role) + " " + unicode(self.role2) + " " + unicode(self.role3)          




class Relationship(models.Model):
	person1 = models.ForeignKey("Person", related_name = "Person1")
	relationship = models.ForeignKey("RelationshipType", blank = True, null = True, related_name = "Relationship Type")
	person2 = models.ForeignKey("Person", related_name = "Person2")

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
	patient_Info = models.ForeignKey("Person", null = True, related_name = "Patient Person Info")
	admitdate = models.CharField("Entry Date", max_length = 15, blank = True)
	exitdate = models.CharField("Departure Date", max_length = 15, blank = True) 
	status = models.TextField("Status on Discharge", blank=True)
	weekly_Rate = models.CharField("Weekly Rate", max_length = 75, blank = True, null = True)
	notes = models.TextField("Note Field", blank = True, null = True)

	
	class Meta:
		verbose_name_plural = "Patient Entries"	


	def __unicode__(self):
		return unicode(self.patient_Info) +  " " + self.admitdate + " " + self.exitdate + " " + self.status + " " +  self.weekly_Rate + " " + self.notes
		


class Biography(models.Model):
	person_Info = models.ForeignKey("Person", related_name = "Bio of Person")
	biography = models.TextField("Bio")
	
	class Meta:
       		verbose_name_plural = "biographies"
	
	def __unicode__(self): 
		return unicode(self.person_Info) + " " + self.biography



class Place(models.Model):
	name = models.CharField("Name of Place", max_length = 50, blank = True, null = True)
	original_Address = models.CharField("Original Address Place", max_length = 150, blank = True, null = True)
	current_Address = models.CharField("Current Address Place", max_length = 150, blank = True, null = True)
	state = models.CharField("State", max_length = 20, blank = True, null = True)
	country = models.CharField("Country", max_length = 20, blank = True, null = True)
	continent = models.CharField("Continent", max_length = 15, blank = True, null = True)
	description = models.TextField("Description Field", blank = True, null = True)
	place_Type = models.ForeignKey("PlaceType", blank = True, null = True, related_name = "Place Type")

	def __unicode__(self):
		return self.name + " " + self.original_Address + " " + self.current_Address + " " + self.state + " " + self.country + " " + self.continent + " " + " " + self.description + " " + unicode(self.place_Type)

class PlaceType(models.Model):
	place_Type = models.CharField("Place Type", max_length = 50, null = True, blank = True)
	description = models.TextField("Place Description", blank = True, null = True)

	class Meta:
       		verbose_name_plural = "Place Types"


	
	def __unicode__(self):
		return self.place_Type + " " + self.description
		



class MeetingtoPersonRelationship(models.Model):
	meeting = models.ForeignKey("Meeting", related_name = "Meeting Information")
	date_Attended = models.CharField("Date of Attendance", max_length = 15, null = True, blank = True)
	person = models.ForeignKey("Person", related_name = "Attending Person")

	class Meta:
       		verbose_name_plural = "Meeting to Person Relationships"

	def __unicode__(self):
		return unicode(self.meeting) + " " + self.date_Attended + " " + unicode(self.person) 

class Meeting(models.Model):
	meeting_Info = models.ForeignKey("Place", related_name = "Meeting Information")
	meeting_Type = models.ForeignKey("MeetingType", null = True, blank = True, related_name = "Meeting Type")

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
	residence = models.ForeignKey("Place", related_name = "Place of Residence")
	date_Lived_There = models.CharField("Date of Residence", max_length = 15, null = True, blank = True)
	person = models.ForeignKey("Person", related_name = "Person Related")
	
	def __unicode__(self):
		return unicode(self.residence) + " " + self.date_Lived_There + " " + unicode(self.person)

class RoleType(models.Model):
	role = models.CharField("Role_Type", max_length = 50, blank = True, null = True)
	description = models.TextField("Description of Role", blank = True, null = True)
	class Meta:
       		verbose_name_plural = "Role Types"


	
	def __unicode__(self):
		return self.role + " " + self.description	
