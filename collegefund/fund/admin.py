from fund.models import Student, Achievement
from django.contrib import admin

class StudentAdmin(admin.ModelAdmin):
    fields = ('user', 'name', 'university',)

admin.site.register(Student, StudentAdmin)
admin.site.register(Achievement)
