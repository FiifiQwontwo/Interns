from django.contrib import admin
from .models import *

# Register your models here.


class AdminLanguages(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('language_name',)}


class FrameworksAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('framework_name',)}


class SchoolNameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_of_university',)}


class InternshipAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('last_name', 'first_name',)}


admin.site.register(Internship, InternshipAdmin)
admin.site.register(SchoolName, SchoolNameAdmin)
admin.site.register(FrameworksAdmin, Frameworks)
admin.site.register(Languages, AdminLanguages)

