from django.contrib import admin
from .models import Gender
from .models import HealthEntity

# Register your models here.
admin.site.register(Gender)
admin.site.register(HealthEntity)
