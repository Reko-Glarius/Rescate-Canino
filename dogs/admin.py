from django.contrib import admin
from .models import Dog

# Register your models here.
class DogsAdmin(admin.ModelAdmin):
    readonly_fields = ['date']

admin.site.register(Dog, DogsAdmin)