from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Product)
admin.site.register(models.Project)

admin.site.site_header = "VDR Admin"
admin.site.site_title = "Connexion"
admin.site.index_title = "A toi de jouer !"