from django.contrib import admin
from . import models


@admin.register(models.Verification)
class VerificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'code')