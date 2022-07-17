from django.shortcuts import render

from meetups.models import Meetups
from meetups.forms import RegistrationForm


# Create your views here.


def index(request):
    meetups = Meetups.objects.all()
    return render(request, 'meetups/index.html', {
        'show_meetup': True,
        'meetups': meetups,
    })


def meetup_detail(request, meetup_slug):
    selected_meetup = Meetups.objects.get(slug=meetup_slug)
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'meetups/meetup-detail.html', {
            'selected_meetup': selected_meetup,
            'form': form
        })
    else:
        form = RegistrationForm(request.POST)  #  takes the posted info from the form in meetup-detail.html and creates an object of
                                               #  participant type (because in the RegistrationForm , the model is Participant)
        if form.is_valid(): # checks to see if the provided data is valid
            participant = form.save()
            selected_meetup.participants.add(participant)

