from django.contrib import admin
from home import models
# Register your models here.

admin.site.register(models.foods)
admin.site.register(models.drinks)
admin.site.register(models.icecreams)