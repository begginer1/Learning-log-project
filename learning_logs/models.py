from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
# Create your models here
    """ text You use CharField when you want to store a small amount of 
    text, such as a name, a title, or a city. When we define a CharField attribute, 
    we have to tell Django how much space it should reserve in the database."""
    text=models.CharField(max_length=200)
    data=models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    """The date_added attribute is a DateTimeField, a piece of data that will 
    record a date and time 2. We pass the argument auto_now_add=True, which 
    tells Django to automatically set this attribute to the current date and time 
    whenever the user creates a new topic."""

    def __str__(self) -> str:
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic."""
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE) # defined topic as foreign key eevery topic has one instance Topic 
    text=models.TextField() # to input text without limit
    date_added=models.DateTimeField(auto_now_add=True)
    """The Meta class holds extra information for managing a model; here, it lets us set a special attribute
    telling Django to use Entries when it needs to refer to more than one entry"""
    class Meta:
        verbose_name_plural = 'entries'
        def __str__(self):
            """Return a simple string representing the entry."""
            return f"{self.text[:50]}..."

    
    