from django.shortcuts import render

from meetups.models import Meetups


# Create your views here.

def index(request):
    meetups = Meetups.objects.all()
    return render(request, 'meetups/index.html', {
        'show_meetup': True,
        'meetups': meetups,
    })


def meetup_detail(request, meetup_slug):
    selected_meetup = Meetups.objects.get(slug=meetup_slug)
    return render(request, 'meetups/meetup-detail.html', {
        'meetup_title': selected_meetup.title,
        'meetup_description': selected_meetup.description,
    })
