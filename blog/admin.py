from django.contrib import admin
from . import models
# Register your models here.


# we can see the date in models.py which is invisible now
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('date', )


admin.site.register(models.BlogModels, BlogAdmin)