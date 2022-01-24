from django.contrib import admin
from .models import City
from .models import Respondent
from .models import Profile
# Register your models here.

admin.site.register(City)
admin.site.register(Respondent)
admin.site.register(Profile)
