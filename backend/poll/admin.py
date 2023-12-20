from django.contrib import admin
from .models import Poll, Choice, Voter

# Register your models here.

class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Voter)
