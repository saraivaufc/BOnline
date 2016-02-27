from django.contrib import admin

from .models import Person, General, Organizer, RegisterKey, OrganizerKey, Occurrence, Report

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	pass
@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
	pass
@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
	pass
@admin.register(OrganizerKey)
class OrganizerKeyAdmin(admin.ModelAdmin):
	pass

@admin.register(Occurrence)
class OccurrenceAdmin(admin.ModelAdmin):
	pass

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
	pass

