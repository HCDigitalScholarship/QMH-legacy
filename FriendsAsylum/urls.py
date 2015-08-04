"""FriendsAsylum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin

from . import views


urlpatterns = [
	url(r'^essay/$', 'FriendsAsylum.views.essay', name = "Framing Essay"),
	url(r'^features/$', 'FriendsAsylum.views.features', name = "Website Features"),
	url(r'^future/$', 'FriendsAsylum.views.future', name = "Future Directions"),
	url(r'^found/$', 'FriendsAsylum.views.found', name = 'Foundation Page'),
	url(r'^profiles/$', 'FriendsAsylum.views.profiles', name = 'Patient Profiles'),
	url(r'^pieq2/$', 'FriendsAsylum.views.pieq2', name = "Pie chart wo philly"),
	url(r'^pieq/$', 'FriendsAsylum.views.pieq', name = "Pie chart of quaker meetings"),
	url(r'^structure/$', 'FriendsAsylum.views.structure', name = 'Structure and Governance'),
	url(r'^religion/$', 'FriendsAsylum.views.religion', name = 'Religion'),
	url(r'^medical/$', 'FriendsAsylum.views.medical', name = 'Medical'),
	url(r'^moral/$', 'FriendsAsylum.views.moral', name = 'Moral'),
	url(r'^occu/$', 'FriendsAsylum.views.occu', name = "Occupational Therapy"),
	url(r'^theology/$', 'FriendsAsylum.views.theology', name = "Theology and Religion"),
	url(r'^york/$', 'FriendsAsylum.views.york', name = "The York Retreat"),
        url(r'^bibliography/$', 'FriendsAsylum.views.bibliography', name = "Bibliography and Credits"),
	url(r'^glossary/$', 'FriendsAsylum.views.glossary', name = 'GlossaryEntry'),
	url(r'^arch/$', 'FriendsAsylum.views.arch', name = 'Architecture Page'),
	url(r'^polls/$', 'FriendsAsylum.views.index', name = 'Index'),
    	url(r'^$', views.Home.as_view(), name = 'home'),
	url(r'^admin/', include(admin.site.urls)),
]

admin.site.site_header = 'Quakers & Mental Health'
admin.site.index_title = 'Quakers & Mental Health Administration'
