from django import forms
from .models import *

class CategoryTypeForm(forms.ModelForm):
    class Meta:
        model = CategoryType
        fields = '__all__'

class CourseTypeForm(forms.ModelForm):
    class Meta:
        model = CourseType
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(EnrollmentForm, self).__init__(*args, **kwargs)
        # Add custom CSS classes to each field
        self.fields['full_name'].widget.attrs.update({'class': 'custom-input', 'placeholder': 'Full Name'})
        self.fields['full_name'].label = ''
        self.fields['mobile_number'].widget.attrs.update({'class': 'custom-input', 'placeholder': 'Mobile Number'})
        self.fields['mobile_number'].label = ''
        self.fields['email'].widget.attrs.update({'class': 'custom-input', 'placeholder': 'Email Address'})
        self.fields['email'].label = ''
        self.fields['message'].widget.attrs.update({'class': 'custom-input', 'placeholder': 'Your Message', 'rows': 1})
        self.fields['message'].label = ''

