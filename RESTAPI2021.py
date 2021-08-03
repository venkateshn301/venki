#!/bin/env/python
# Sample Django Restframework
# django -admin startproject pname
# python manage.py startapp appname
# python manage.py runserver 
# HTTP Request methods are GET,POST,HEAD,PUT,DELETE AND PATCH--Update individual fileds
# https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c

#pname/settings.py
INSTALLED_APPS=[
    'applicationname'
    
]
# python manage.py migrate
# Django default models will get migrated to ourDb else DJ default Db SQLite
# Creating Superuser
# python manage.py createsuperuser name
# using above credetials you can login django admin dasboard
# Creating django models
#Inside appln /mpdels.py

from django.db import models
class Hero(models.Model):
    name=models.charField(max_length=100)
    alias_name = models.charField(max_length=100)
    #__str__ method just tells Django what to print when it needs to print out an instance of the Hero model.
    def __str__(self):
        return self.name
#Remember, whenever we define or change a model, we need to tell Django to migrate those changes.
python manage.py makemigrations
#appname/admin.py
from django.contrib import admin
from .models import Hero
admin.site.register('Hero')

#Now run the servere
Python manage.py runserver
#We can see application dashboard.Here we can add new user or delete existing user

#To serialize class models we have to install restframework
pip install djangorestframework

#Once installed we have to configure in pname/settings.py
INSTALLED_APPS=[
    'rest_framework'
]
#It's time to serialize our model
# We have to new file called appln/serializers.py
#file content 
#Serialize the Hero model

from rest_framework import serializers
from.models import Hero

class Heroserializers(serializers.HyperlinkedmodelSeralizer):
    class Meta:
        model=Hero
        fileds=('id','name','alias_name')
#Display model data
appname/views.py
from rest_framework import viewsets
from .models import Hero
from .serializers import Heroserializers
#ModelViewSet is a special view that Django Rest Framework provides. 
#It will handle GET and POST for Heroes without us having to do any more work.
class heroviewset(viewsets.ModelViewSet):
    query_set=Hero.object.all().order_by('name')
    serializer_class=Heroserializers


#Site URL's

from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appurls.urls')),
 ]

# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] 

# python manage.py runserver
http://127.0.0.1:8000/heroes/1/