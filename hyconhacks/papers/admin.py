from django.contrib import admin
from . import models

@admin.register(models.Paper)
class PaperAdmin(admin.ModelAdmin):

    list_display = (
        "segment",
        "target",
        "file_path",
        "sender",
        "receiver",
        "incentive",
        "difficulty",
    )
