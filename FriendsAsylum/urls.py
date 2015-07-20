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
	url(r'^foundation/$', 'FriendsAsylum.views.foundation', name = 'Foundation Page'),
	url(r'^profiles/$', 'FriendsAsylum.views.profiles', name = 'Patient Profiles'),
	url(r'^struct$', 'FriendsAsylum.views.struct', name = 'Structure and Governance'),
	url(r'^patient/$', 'FriendsAsylum.views.patient', name = 'Patient Info'),
	url(r'^glossary/$', 'FriendsAsylum.views.glossary', name = 'GlossaryEntry'),
	url(r'^arch/$', 'FriendsAsylum.views.arch', name = 'Architecture Page'),
	url(r'^polls/$', 'FriendsAsylum.views.index', name = 'Index'),
    	url(r'^$', views.Home.as_view(), name = 'home'),
	url(r'^admin/', include(admin.site.urls)),
]

admin.site.site_header = 'Quakers & Mental Health'
admin.site.index_title = 'Quakers & Mental Health Administration'
