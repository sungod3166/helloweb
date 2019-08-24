from django.shortcuts import render
from .models import Topic
from django.db import models


# Create your views here.
def index(request):
    return render(request,"djangoapps/index.html")
def topics(request):
    topics=Topic.objects.order_by('date_added')
    context = {}
    context['hello'] = topics
    return render(request,'djangoapps/topics.html',context)
def topic(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'djangoapps/topic.html',context)