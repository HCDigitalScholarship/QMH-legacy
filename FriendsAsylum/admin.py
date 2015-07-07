
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources 
from FriendsAsylum.models import Person, Relationship, RelationshipType, PatientEntry, Biography, Place, PlaceType, MeetingtoPersonRelationship, Meeting, MeetingType, Residence, RoleType

class PersonResource(resources.ModelResource):
	class Meta:
		model = Person
		fields = ('id', 'first_name', 'last_name', 'alias', 'birth', 'death', 'gender', 'birthplace', 'role', 'role2', 'role3')


#class MyAdminSite(AdminSite):
#site_header = "Friends Asylum Administration"
#site_title = "Friends Asylum Admin"

class PersonAdmin(ImportExportModelAdmin):
	fields = ['first_name', 'last_name', 'alias', 'birth', 'death', 'gender', 'birthplace', 'role', 'role2', 'role3']
	resource_class = PersonResource
	pass

class RelationshipResource(resources.ModelResource):
	class Meta:
		model = Relationship
		fields = ('id', 'person1', 'relationship', 'person2')

class RelationshipAdmin(ImportExportModelAdmin):
	fields = ['person1', 'relationship', 'person2']
	resource_class = RelationshipResource
	pass


class PatientEntryResource(resources.ModelResource):
	class Meta:
		model = PatientEntry
		fields = ('id', 'patient_Info', 'admitdate', 'exitdate', 'status', 'weekly_Rate', 'notes') 

class PatientEntryAdmin(ImportExportModelAdmin):
	fields = ['patient_Info', 'admitdate', 'exitdate', 'status', 'weekly_Rate', 'notes']
	resource_class = PatientEntryResource
	pass 

class BiographyResource(resources.ModelResource):
	class Meta:
		model = Biography
		fields = ('id', 'person_Info', 'biography')


class BiographyAdmin(ImportExportModelAdmin):
	fields = ['person_Info', 'biography']
	resource_class = BiographyResource
	pass

class RelationshipTypeResource(resources.ModelResource):
	class Meta:
		model = RelationshipType
		fields = ('id', 'relationship_Type', 'description')

class RelationshipTypeAdmin(ImportExportModelAdmin):
	fields = ['relationship_Type', 'description']
	resource_class = RelationshipTypeResource
	pass




class PlaceResource(resources.ModelResource):
	class Meta:
		model = Place
		fields = ('id', 'name', 'original_Address', 'current_Address', 'state', 'country', 'continent', 'description', 'place_Type')
	
class PlaceAdmin(ImportExportModelAdmin):
	fields = ['name', 'original_Address', 'current_Address', 'state', 'country', 'continent', 'description', 'place_Type']
	resource_class = PlaceResource
	pass

class PlaceTypeResource(resources.ModelResource):
	class Meta:
		model = PlaceType
		fields = ('id', 'place_Type', 'description')


class PlaceTypeAdmin(ImportExportModelAdmin):
	fields = ['place_Type', 'description']
	resource_class = PlaceTypeResource
	pass

class MeetingtoPersonRelationshipResource(resources.ModelResource):
	class Meta:
		model = MeetingtoPersonRelationship
		fields = ('id', 'meeting', 'date_Attended', 'person')


class MeetingtoPersonRelationshipAdmin(ImportExportModelAdmin):
	fields = ['meeting', 'date_Attended', 'person']
	resource_class = MeetingtoPersonRelationshipResource
	pass

class MeetingResource(resources.ModelResource):
	class Meta:
		model = Meeting
		fields = ('id', 'meeting_Info', 'meeting_Type')


class MeetingAdmin(ImportExportModelAdmin):
	fields = ['meeting_Info', 'meeting_Type']
	resource_class = MeetingResource	
	pass

class MeetingTypeResource(resources.ModelResource):
	class Meta:
		model = MeetingType
		fields = ('id', 'meeting_Type', 'description')

class MeetingTypeAdmin(ImportExportModelAdmin):
	fields = ['meeting_Type', 'description']
	resource_class = MeetingTypeResource
	pass


class ResidenceResource(resources.ModelResource):
	class Meta:
		model = Residence
		fields = ('id', 'residence', 'date_Lived_There', 'person')


class ResidenceAdmin(ImportExportModelAdmin):
	fields = ['residence', 'date_Lived_There', 'person']
	resource_class = ResidenceResource
	pass


class RoleTypeResource(resources.ModelResource):
	class Meta:
		model = RoleType
		fields = ('id', 'role', 'description')

class RoleTypeAdmin(ImportExportModelAdmin):
	fields = ['role', 'description']
	resource_class = RoleTypeResource
	pass


#admin_site = MyAdminSite(name = 'myadmin')
admin.site.register(Person,PersonAdmin)
admin.site.register(Relationship,RelationshipAdmin)
admin.site.register(RelationshipType,RelationshipTypeAdmin)
admin.site.register(PatientEntry,PatientEntryAdmin)
admin.site.register(Biography,BiographyAdmin)
admin.site.register(Place,PlaceAdmin)
admin.site.register(PlaceType,PlaceTypeAdmin)
admin.site.register(MeetingtoPersonRelationship,MeetingtoPersonRelationshipAdmin)
admin.site.register(Meeting,MeetingAdmin)
admin.site.register(MeetingType,MeetingTypeAdmin)
admin.site.register(Residence,ResidenceAdmin)
admin.site.register(RoleType,RoleTypeAdmin)

