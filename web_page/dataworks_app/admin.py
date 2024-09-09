from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(CategoryType)
admin.site.register(Course)
admin.site.register(CourseType)
admin.site.register(Blog_Page)
admin.site.register(Blog_List)
admin.site.register(recommended_course)