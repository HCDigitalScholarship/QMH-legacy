from django.db import models

 

class Person(models.Model):
	first_name = models.CharField("First Name", max_length=100)
	last_name = models.CharField("Last Name", max_length=100)
	alias = models.CharField("Alias Name", max_length = 100, blank = True, null =True) #only needed for patients
	birth = models.CharField("Birth Date", max_length=20, blank = True)
	death =  models.CharField("Death Date", max_length=20, blank = True)
	gender =  models.CharField("Gender", blank = True, null = True,  max_length=20)
	birthplace = models.ForeignKey("Place", blank = True, null = True, related_name = "birth_place")
	role = models.ForeignKey("RoleType", blank =True, null=True, related_name = '%(class)s_Role_1')
	role2 = models.ForeignKey("RoleType", blank = True, null= True, related_name = '%(class)s_Role_2')
	role3 = models.ForeignKey("RoleType", blank = True, null=True, related_name = '%(class)s_Role_3')

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
	duration = models.IntegerField("Duration of Insanity/Disease", blank = True, null = True, help_text = "Enter duration of insanity in number of days")
	weekly_Rate = models.CharField("Weekly Rate", max_length = 75, blank = True, null = True)
	notes = models.TextField("Note Field", blank = True, null = True)
	age = models.CharField("Age at Admittance", default = '', max_length = 3, null = True, blank = True)	
	
	class Meta:
		verbose_name_plural = "Patient Entries"	


	def __unicode__(self):
		return unicode(self.patient_Info) +  " " +  self.admitdate + " " + self.exitdate + " " + self.status + " " +  self.weekly_Rate + " " + self.notes + " " + self.age + " " + unicode(self.duration)

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
	role = models.CharField("Role_Type", max_length = 50, null = True, blank = True)
	description = models.TextField("Description of Role", null = True, blank = True)
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

class Text_Entry(models.Model):
	text = models.ForeignKey("Text", null = True, blank = True)
	page_Number = models.CharField("Page Number", max_length = 35, blank = True, null = True)
	date = models.DateField("Date of Entry", null = True, blank = True)
	table = models.NullBooleanField("Table", null = True, help_text = "Select whatever form type most closely corresponds to the text entry you are working with.  Either select one or none.")
	table_columns = models.CharField("Table Columns", max_length = 500, null = True, blank = True, help_text = "Please separate all column values you find with commas.For example: age, height, eye color, etc.")
	table_rows = models.CharField("Table Rows", max_length = 500, null = True, blank = True, help_text = "Please separate all row values you find with commas.For example: age, height, eye color, etc.")
	fill_In = models.NullBooleanField("Fill in the Blanks", null = True, help_text = "This type of form often has blank spaces '____' for a physician to write the patient's name, gender, etc.")
	fillvals = models.CharField("Fill in Values", max_length = 500, null = True, blank = True, help_text = "Please write out what content any blank spaces in the form you are working with is supposed to have. For example, if a doctor is supposed to fill in information about name, age, sex, write: 'name, age, sex'")
	free_Form = models.NullBooleanField("Free Form", null = True, help_text = "You can use this field if the form of the entry you are working with is not like a table or a fill in the blank type")
	details = models.TextField("Relevant Information or Details", null = True, blank = True, help_text = "Use this text editor to add important details about the entry you are working with, or if you are working with a free form entry type, this is where you will write what it is about")

	class Meta:
        	verbose_name_plural = "Text Entries"

	def __unicode__(self):
		return unicode(self.text) + " " + self.page_Number + " " + unicode(self.date) + " " + self.table + " " + self.table_rows + " " + self.table_columns + " " + self.fill_In + " " + self.fillvals + " " + self.free_Form + " " + self.details

class PersonChoice(models.Model):
	text_Entry = models.ForeignKey("Text_Entry", null = True, blank = True)
	person = models.ForeignKey("Person", null = True, blank = True)

	def __unicode__(self):
		return unicode(self.text_Entry) + " " + unicode(self.person)
