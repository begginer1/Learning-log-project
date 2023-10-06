"""Defines URL patterns for learning_logs."""
from django.urls import path  
"""We then import the path function, which is needed when mapping URLs to views""",
from . import views   
app_name='learning_logs'

"""The variable app_name helps Django 
distinguish this urls.py file from files of the same name in other apps within 
the project"""
urlpatterns =[  #The variable urlpatterns in this module is a list of individual pages that can be requested from the learning_logs app 
    # Home page  
   path('', views.index, name='index'), # first argument is the url if which is added to django when when reuest to url made
        #second argument is  specifies which function to call 
        #in views.py. When a requested URL matches the pattern we’re defining, 
        #Django calls the index() function from views.py"""

        #The third argument provides the name index for 
        #this URL pattern so we can refer to it more easily in other files throughout 
        #the project. Whenever we want to provide a link to the home page, we’ll use 
        #this name instead of writing out a URL."""
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    #Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]