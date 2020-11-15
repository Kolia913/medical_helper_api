from django.contrib import admin
from .models import Type, Disease, Pill, Conflict, Effect
# Register your models here.

admin.site.register(Type)
admin.site.register(Disease)
admin.site.register(Pill)
admin.site.register(Conflict)
admin.site.register(Effect)
