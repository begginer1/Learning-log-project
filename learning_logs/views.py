from django.shortcuts import render,redirect
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

"""The render() function here passes two arguments: the original request object and 
a template it can use to build the page. Let’s write this template"""

@login_required # decorator to see topic by regised user
def topics(request):
    #Show all topics.
    topics = Topic.objects.order_by('data') # pass al Topic class object
    topics = Topic.objects.filter(owner=request.user).order_by('data')
    context = {'topics': topics} 
    #A context is a dictionary in which the keys are names we’ll use in the template to access 
    #the data we want, and the values are the data we need to send to the template"""
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request,topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added') # - means in reverrse order
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            form.save()
            return redirect('learning_logs:topics')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
    # No data submitted; create a blank form.
        form = EntryForm()
    else:
    # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) # to save in new_entry but not commit to database yet 
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id) # redirect to view topic with id is topic id
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request,entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method!='POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
        