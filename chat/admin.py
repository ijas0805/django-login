from django.contrib import admin
from django.http.request import RawPostDataException
from .models import Room, Message

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
