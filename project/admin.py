from django.contrib import admin
from .models import Member, Book, Meeting, ReadingProgress

# Register your models here.
admin.site.register(Member)
admin.site.register(Book)
admin.site.register(Meeting)
admin.site.register(ReadingProgress)