from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(CategoryType)
admin.site.register(Course)
admin.site.register(CourseType)
admin.site.register(Blog_Page)
admin.site.register(Blog_List)
admin.site.register(recommended_course)
admin.site.register(CourseInfo)
admin.site.register(course_content)
admin.site.register(HiringPartner)
admin.site.register(Tool)
admin.site.register(CourseRequirement)
admin.site.register( FAQs)
admin.site.register(CourseCertificate)
admin.site.register( Review)
admin.site.register(CourseRating)
