from django.contrib import admin
from .models import*

# Register your models here.
admin.site.register(Site)
admin.site.register(MaterialReport)
admin.site.register(MachineryReport)
admin.site.register(SiteExpenseReport)