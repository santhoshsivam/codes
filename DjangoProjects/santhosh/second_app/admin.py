from django.contrib import admin
from .models import baby
from .models import santhosh
from second_app import models
# Register your models here.
admin.site.register(baby)
admin.site.register(santhosh)
admin.site.register(models.mistorminor)
