from django.contrib import admin
from .models import Country, State, City, Institution, Department, Course, Stream, Semester, Subject

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ('country',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    list_filter = ('state',)

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    list_filter = ('city',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution')
    list_filter = ('institution',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    list_filter = ('department',)

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'course')
    list_filter = ('course',)

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('number', 'stream')
    list_filter = ('stream',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'semester')
    list_filter = ('semester',)
