# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('biography', models.TextField(verbose_name=b'Bio')),
            ],
            options={
                'verbose_name_plural': 'biographies',
            },
        ),
        migrations.CreateModel(
            name='GeoPlace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Glossary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=100, null=True, verbose_name=b'Word', blank=True)),
                ('definition', models.TextField(null=True, verbose_name=b'Definition of Word', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Glossary',
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingtoPersonRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_Attended', models.CharField(max_length=15, null=True, verbose_name=b'Date of Attendance', blank=True)),
                ('meeting', models.ForeignKey(to='FriendsAsylum.Meeting')),
            ],
            options={
                'verbose_name_plural': 'Meeting to Person Relationships',
            },
        ),
        migrations.CreateModel(
            name='MeetingType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meeting_Type', models.CharField(max_length=75, verbose_name=b'Meeting Type')),
                ('description', models.TextField(null=True, verbose_name=b'Description of Meeting', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Meeting Types',
            },
        ),
        migrations.CreateModel(
            name='PatientEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('admitdate', models.CharField(max_length=15, verbose_name=b'Entry Date', blank=True)),
                ('exitdate', models.CharField(max_length=15, verbose_name=b'Departure Date', blank=True)),
                ('status', models.TextField(verbose_name=b'Status on Discharge', blank=True)),
                ('weekly_Rate', models.CharField(max_length=75, null=True, verbose_name=b'Weekly Rate', blank=True)),
                ('notes', models.TextField(null=True, verbose_name=b'Note Field', blank=True)),
                ('age', models.CharField(max_length=3, null=True, verbose_name=b'Age at Admittance', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Patient Entries',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100, verbose_name=b'First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name=b'Last Name')),
                ('alias', models.CharField(max_length=100, null=True, verbose_name=b'Alias Name', blank=True)),
                ('birth', models.CharField(max_length=20, verbose_name=b'Birth Date', blank=True)),
                ('death', models.CharField(max_length=20, verbose_name=b'Death Date', blank=True)),
                ('gender', models.CharField(max_length=20, null=True, verbose_name=b'Gender', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name=b'Name of Place', blank=True)),
                ('original_Address', models.CharField(max_length=150, null=True, verbose_name=b'Original Address Place', blank=True)),
                ('current_Address', models.CharField(max_length=150, null=True, verbose_name=b'Current Address Place', blank=True)),
                ('state', models.CharField(max_length=20, null=True, verbose_name=b'State', blank=True)),
                ('country', models.CharField(max_length=20, null=True, verbose_name=b'Country', blank=True)),
                ('continent', models.CharField(max_length=15, null=True, verbose_name=b'Continent', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Description Field', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place_Type', models.CharField(max_length=50, null=True, verbose_name=b'Place Type', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Place Description', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Place Types',
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person1', models.ForeignKey(related_name='relationship_Person_1', to='FriendsAsylum.Person')),
                ('person2', models.ForeignKey(related_name='relationship_Person_2', to='FriendsAsylum.Person')),
            ],
        ),
        migrations.CreateModel(
            name='RelationshipType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relationship_Type', models.CharField(max_length=50, null=True, verbose_name=b'Relationship Type', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Description (if necessary)', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Relationship Types',
            },
        ),
        migrations.CreateModel(
            name='Residence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_Lived_There', models.CharField(max_length=15, null=True, verbose_name=b'Date of Residence', blank=True)),
                ('person', models.ForeignKey(to='FriendsAsylum.Person')),
                ('residence', models.ForeignKey(to='FriendsAsylum.Place')),
            ],
        ),
        migrations.CreateModel(
            name='RoleType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=50, null=True, verbose_name=b'Role_Type', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Description of Role', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Role Types',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name=b'Name of Text', blank=True)),
                ('volume', models.CharField(max_length=4, null=True, verbose_name=b'Vol. #', blank=True)),
                ('dates', models.CharField(max_length=40, null=True, verbose_name=b'Dates of Text', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Description of Text', blank=True)),
                ('author', models.ForeignKey(related_name='text_Author', blank=True, to='FriendsAsylum.Person', null=True)),
                ('clerk', models.ForeignKey(related_name='text_Clerk', blank=True, to='FriendsAsylum.Person', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Text_Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person1', models.ForeignKey(related_name='text_relationship_Person_1', blank=True, to='FriendsAsylum.Person', null=True)),
                ('person10', models.ForeignKey(related_name='text_relationship_Person_10', blank=True, to='FriendsAsylum.Person', null=True)),
                ('person11', models.ForeignKey(related_name='text_relationship_Person_11', blank=True, to='FriendsAsylum.Person', null=True)),
                ('person12', models.ForeignKey(related_name='text_relationship_Person_12', blank=True, to='FriendsAsylum.Person', null=True)),
                ('person13', models.ForeignKey(related_name='text_relationship_Person_13', blank=True, to='FriendsAsylum.Person', null=True)),
                ('person14', models.ForeignKey(related_name='text_relationship_Person_14', blank=True, to='FriendsAsylum.Person', null=True)),
                ('person15', models.ForeignKey(related_name='text_relationship_Person_15', blank=True, to='FriendsAsylum.Person', null=True)),
                ('person2', models.ForeignKey(related_name='text_relationship_Person_2', blank=True, to='FriendsAsylum.Person', null=True)),
                ('person3', models.ForeignKey(related_name='text_relationship_Person_3', blank=True, to='FriendsAsylum.Person', null=True)),
                ('person4', models.ForeignKey(related_name='text_relationship_Person_4', blank=True, to='FriendsAsylum.Person', null=True)),
                ('person5', models.ForeignKey(related_name='text_relationship_Person_5', blank=True, to='FriendsAsylum.Person', null=True)),
                ('person6', models.ForeignKey(related_name='text_relationship_Person_6', blank=True, to='FriendsAsylum.Person', null=True)),
                ('person7', models.ForeignKey(related_name='text_relationship_Person_7', blank=True, to='FriendsAsylum.Person', null=True)),
                ('person8', models.ForeignKey(related_name='text_relationship_Person_8', blank=True, to='FriendsAsylum.Person', null=True)),
                ('person9', models.ForeignKey(related_name='text_relationship_Person_9', blank=True, to='FriendsAsylum.Person', null=True)),
                ('text', models.ForeignKey(blank=True, to='FriendsAsylum.Text', null=True)),
            ],
            options={
                'verbose_name_plural': 'Text Relationship Types',
            },
        ),
        migrations.CreateModel(
            name='Text_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text_Type', models.CharField(max_length=100, null=True, verbose_name=b'Text Type', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Description of Text', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Text Types',
            },
        ),
        migrations.AddField(
            model_name='text',
            name='text_Type',
            field=models.ForeignKey(blank=True, to='FriendsAsylum.Text_Type', null=True),
        ),
        migrations.AddField(
            model_name='relationship',
            name='relationship',
            field=models.ForeignKey(blank=True, to='FriendsAsylum.RelationshipType', null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='place_Type',
            field=models.ForeignKey(blank=True, to='FriendsAsylum.PlaceType', null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='birthplace',
            field=models.ForeignKey(related_name='birth_place', blank=True, to='FriendsAsylum.Place', null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.ForeignKey(related_name='person_Role_1', blank=True, to='FriendsAsylum.RoleType', null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='role2',
            field=models.ForeignKey(related_name='person_Role_2', blank=True, to='FriendsAsylum.RoleType', null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='role3',
            field=models.ForeignKey(related_name='person_Role_3', blank=True, to='FriendsAsylum.RoleType', null=True),
        ),
        migrations.AddField(
            model_name='patiententry',
            name='patient_Info',
            field=models.ForeignKey(to='FriendsAsylum.Person', null=True),
        ),
        migrations.AddField(
            model_name='meetingtopersonrelationship',
            name='person',
            field=models.ForeignKey(to='FriendsAsylum.Person'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_Info',
            field=models.ForeignKey(to='FriendsAsylum.Place'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_Type',
            field=models.ForeignKey(blank=True, to='FriendsAsylum.MeetingType', null=True),
        ),
        migrations.AddField(
            model_name='geoplace',
            name='place_Info',
            field=models.ForeignKey(blank=True, to='FriendsAsylum.Place', null=True),
        ),
        migrations.AddField(
            model_name='biography',
            name='person_Info',
            field=models.ForeignKey(to='FriendsAsylum.Person'),
        ),
    ]
