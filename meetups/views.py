from django.shortcuts import render


# Create your views here.

def index(request):
    meetups = [
        {'title': 'a first meetup'},
        {'title': 'a second meetup'}
    ]
    return render(request, 'meetups/index.html', {
        'show_meetup': True,
        'meetups': meetups
    })

