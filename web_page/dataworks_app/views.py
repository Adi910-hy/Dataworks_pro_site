from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from bs4 import BeautifulSoup # type: ignore
import re

def create_category(request):
    if request.method == 'POST':
        form = CategoryTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryTypeForm()
    return render(request, 'category_form.html', {'form': form})

def category_list(request):
    categories = CategoryType.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_types_list')
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form})

def course_list(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        return render(request, 'course_list.html', {'courses': courses})

def create_course_type(request):
    if request.method == 'POST':
        form = CourseTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_types_list')
    else:
        form = CourseTypeForm()
    return render(request, 'create_course_type.html', {'form': form})
    
def course_types_list(request):
    types = CourseType.objects.all()
    return render(request, 'course_types_list.html', {'types': types})

def course_by_type(request, pk):
    type_instance = get_object_or_404(CourseType, pk=pk)
    courses = Course.objects.filter(category=type_instance)[:5]
    return render(request, 'course_by_type.html', {'type': type_instance, 'courses': courses})

def enrollment_success(request):
    return render(request, 'enrollment_success.html')

def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_form.html', {'form': form})

def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_types_list')
    return render(request, 'course_confirm_delete.html', {'object': course})

def course_type_detail(request, course_type_id):
    course_type = get_object_or_404(CourseType, id=course_type_id)
    courses = Course.objects.filter(category=course_type)

    return render(request, 'course_type_detail.html', {
        'course_type': course_type,
        'courses': courses,
    })

def foundations_test(request, course_type_id=None):
    if course_type_id:
        course_type = get_object_or_404(CourseType, id=course_type_id)
        courses = Course.objects.filter(category=course_type)
    else:
        courses = Course.objects.all()
    
    course_types = CourseType.objects.all()
    return render(request, 'foundations_test.html', {
        'courses': courses,
        'course_types': course_types,
        'selected_course_type_id': course_type_id,
    })

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course_contents = course.course_content.all()
    faqs = course.faqs.all()
    reviews = course.reviews.all()
    hiring_partners = HiringPartner.objects.all()
    tools = Tool.objects.all()
    requirements = course.requirements.all()
    course_outcomes = course.course_info.all()
    certificate = getattr(course, 'certificate', None)
    rating = CourseRating.objects.filter(course=course).first()
    demo_request = DemoRequest.objects.first()
    mentions = recommended_course.objects.all()
    success_message = None

    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "You have successfully enrolled."
            form = EnrollmentForm()
            # return redirect('enrollment_success')
    else:
        form = EnrollmentForm()

    return render(request, 'coursepage_testing.html', {
        'course_page': course,
        'form': form,
        'course_contents': course_contents,
        'faqs': faqs,
        'reviews': reviews,
        'hiring_partners': hiring_partners,
        'tools': tools,
        'requirements': requirements,
        'course_outcomes': course_outcomes,
        'certificate': certificate,
        'rating': rating,
        'demo_request': demo_request,
        'success_message': success_message,
        'mentions': mentions,
    })

def category_course(request):
    course_type_id = request.GET.get('course_type_id')

    categories = CategoryType.objects.all()

    course_types = CourseType.objects.all()

    courses = Course.objects.all()
    mentions = recommended_course.objects.all()

    return render(request, 'home.html', {
        'categories': categories,
        'course_types': course_types,
        'courses': courses,
        'mentions': mentions,
    })

def corporate_view(request):
    return render(request, 'corporate_page.html')

def blog_detail(request, pk):
    post = get_object_or_404(Blog_Page, pk=pk)
    blogs = Blog_Page.objects.all()
    content = Blog_List.objects.first()
    soup = BeautifulSoup(post.content_description, 'html.parser')
    sections = []

    for i, tag in enumerate(soup.find_all(re.compile('^h[1-6]$'))):
        heading_id = f'section-{i+1}'
        tag['id'] = heading_id
        sections.append({
            'id': heading_id,
            'heading': tag.get_text(),
            'level': tag.name,
            'content': str(tag) + str(tag.find_next_sibling())
        })

    updated_content = str(soup)

    for blog in blogs:
        soup = BeautifulSoup(blog.content_description, 'html.parser')
        first_image_tag = soup.find('img')
        blog.image_url = first_image_tag['src'] if first_image_tag else None
        blog.truncated_description = extract_first_50_words(blog.content_description)

    return render(request, 'blog_detail.html', {
        'post': post,
        'blogs': blogs,
        'content': content,
        'sections': sections,
        'updated_content': updated_content
    })

def extract_first_50_words(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    words = text.split()
    return ' '.join(words[:50]) + '...' if len(words) > 50 else text

def blog_list_view(request):
    content = Blog_List.objects.first()
    blogs = Blog_Page.objects.all()
    courses = Course.objects.all()

    for blog in blogs:
        soup = BeautifulSoup(blog.content_description, 'html.parser')
        first_image_tag = soup.find('img')
        blog.image_url = first_image_tag['src'] if first_image_tag else None
        blog.truncated_description = extract_first_50_words(blog.content_description)

    return render(request, 'blog_list.html', {
        'content': content,
        'blogs': blogs,
        'courses': courses,
        })

def blog_header_view(request):
    categories = CategoryType.objects.all()
    course_types = CourseType.objects.all()
    courses = Course.objects.all()

    return render(request, 'base.html', {
        'categories': categories,
        'course_types': course_types,
        'courses': courses,
        })