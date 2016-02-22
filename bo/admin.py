from django.contrib import admin

from .models import Person, GeneralUser, Organizer, RegisterKey, OrganizerKey

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	pass
@admin.register(GeneralUser)
class GeneralUserAdmin(admin.ModelAdmin):
	pass
@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
	pass
@admin.register(OrganizerKey)
class OrganizerKeyAdmin(admin.ModelAdmin):
	pass

