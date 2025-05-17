from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Club)
admin.site.register(Filial)
admin.site.register(Staff)

