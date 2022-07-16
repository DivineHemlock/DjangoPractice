from django.contrib import admin

from meetups.models import Meetups, Location
# Register your models here.


class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image')
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Meetups, MeetupAdmin)
admin.site.register(Location)
