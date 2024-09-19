from django.contrib import admin
from .models import Services, Advertisements, Profile, Contracts

# Register your models here.
admin.site.register(Services)
admin.site.register(Advertisements)
admin.site.register(Profile)
admin.site.register(Contracts)