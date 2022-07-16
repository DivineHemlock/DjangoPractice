from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from meetups import views

urlpatterns = [
    path('meetups/', views.index, name='all-meetups'),  # our-domain.com/meetups
    path('meetups/<slug:meetup_slug>', views.meetup_detail, name='meetup-detail')  # our-domain.com/meetups/<dynamic-path>
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
