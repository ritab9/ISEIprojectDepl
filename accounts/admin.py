from django.contrib import admin

# Register your models here.

from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin


class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False


class UserAdmin(AuthUserAdmin):
    inlines = [TeacherInline]
    list_display = ('id','username', 'first_name', 'last_name')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(School)
class School(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'school_code')
    list_editable = ( 'abbreviation', 'school_code')

@admin.register(SchoolYear)
class SchoolYear(admin.ModelAdmin):
    list_display = ('name','active_year')
    list_editable = ('active_year',)
    list_display_links = ('name',)

@admin.register(PDAType)
class PDAType(admin.ModelAdmin):
    list_display = ('category', 'type', 'ceu_value')
    fields = ['category', 'type', 'ceu_value']


class PDAInstanceInline(admin.StackedInline):
    model = PDAInstance
    can_delete = False
    extra = 1


@admin.register(PDARecord)
class PDARecord(admin.ModelAdmin):
    inlines = [PDAInstanceInline]
    list_display = ('teacher', 'school_year', 'date_submitted','principal_signed')
    list_editable = ('date_submitted', 'principal_signed')
    list_display_links = ('teacher',)
