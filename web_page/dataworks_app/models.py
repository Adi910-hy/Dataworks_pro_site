from django.db import models

class CategoryType(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('parent', 'name')
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name 
    
class CourseType(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(CategoryType, on_delete=models.CASCADE, related_name='course_types', null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('parent', 'name')
        verbose_name_plural = 'course types'

    def __str__(self):
        return self.name 

class Course(models.Model):
    category = models.ForeignKey(CourseType, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=100)
    description = models.TextField()
    topic_image = models.ImageField()
    gif_image = models.ImageField()
    header_image = models.ImageField()

    def __str__(self):
        return self.title
    
class course_content(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_content')
    heading = models.CharField(max_length=250)
    key_points = models.TextField()

class FAQs(models.Model):
    faq = models.ForeignKey(Course, on_delete=models.CASCADE, related_name= 'faqs')
    faq_heading = models.CharField(max_length=250)
    faq_description = models.TextField()

class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    reviewer_image = models.ImageField()
    review_text = models.TextField()
    star_rating = models.PositiveIntegerField()

class HiringPartner(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='partner_images')
    name = models.CharField(max_length=100)
    logo = models.ImageField()

class Enrollment(models.Model):
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()

class Tool(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tools')
    tool_name = models.CharField(max_length=100)
    image = models.ImageField()

class CourseRequirement(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='requirements')
    requirement = models.TextField()

class CourseInfo(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_info')
    outcome_text = models.TextField()

class CourseCertificate(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='certificate')
    description = models.TextField()
    image = models.ImageField()

class CourseRating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ratings')
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    num_ratings = models.PositiveIntegerField()
    brochure_url = models.URLField()

class DemoRequest(models.Model):
    paragraph_text = models.TextField()
    button_text = models.CharField(max_length=100)
    button_url = models.URLField()

class recommended_course(models.Model):
    image = models.ImageField()
    point1 = models.CharField(max_length=150)
    point2 = models.CharField(max_length=150)
    course_title = models.CharField(max_length=50)

class Blog_Page(models.Model):
    heading = models.CharField(max_length=255)
    quote = models.TextField()
    content_description = models.TextField()
    advertisement = models.ImageField()

class Blog_List(models.Model):
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    text = models.TextField()
    placeholder_email = models.EmailField()
    button_text = models.CharField(max_length=50)
    background_image = models.ImageField()
    popular_blog_title = models.CharField(max_length=50)
    popular_blog_mini_title = models.TextField()
    blog_author = models.TextField()
    publish_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title1


