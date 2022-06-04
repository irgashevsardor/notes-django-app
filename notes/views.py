from django.shortcuts import render
from .models import Topic, Entry


def index(request):
    return render(request, 'notes/home_page.html')


def topics(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'notes/topics.html', context=context)


def entries(request, topic_id):
    topic_entries = Topic.objects.get(id=topic_id).entry_set.order_by('-date_added')
    context = {'entries': topic_entries}
    return render(request, 'notes/entries.html', context=context)
