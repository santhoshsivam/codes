from django.contrib import admin
from .models import questions
from mainapp_2 import models
# Register your models here.


admin.site.register(questions)
admin.site.register(models.fifth_standard)
admin.site.register(models.sixth_standard)
admin.site.register(models.seventh_standard)
admin.site.register(models.signin)
