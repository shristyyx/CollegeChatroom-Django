from django.contrib import admin

# Register your models here.
from .models import Room, City, Message

admin.site.register(Room)
admin.site.register(City)
admin.site.register(Message)