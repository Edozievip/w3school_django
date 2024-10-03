from django.contrib import admin
from .models import Member

# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "lastname", "age", "phone")

admin.site.register(Member, MemberAdmin)

