from django.contrib import admin
from . import models

# Yaratgan tablelarimizni sayt admindan ro`yxatdan o`tkazadi

admin.site.register(models.Contact)
admin.site.register(models.Service)
admin.site.register(models.Blog)
admin.site.register(models.Sponsour)
admin.site.register(models.Portfolio)
admin.site.register(models.Team)
