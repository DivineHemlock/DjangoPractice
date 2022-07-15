from django.shortcuts import render


# Create your views here.

def index(request):
    meetups = [
        {'title': 'a first meetup',
         'location': 'paris',
         'slug': 'a-first-meetup'},

        {'title': 'a second meetup',
         'location': 'new york',
         'slug': 'a-second-meetup'}
    ]
    return render(request, 'meetups/index.html', {
        'show_meetup': True,
        'meetups': meetups
    })


def meetup_details(request , meetup_slug):
    selected_meetup = {
        'title': 'first meetup',
        'description': 'details are displayed here for the meetup!'
    }
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })
