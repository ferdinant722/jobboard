from django import forms
from .models import Job
from .models import JobApplication
# jobs/forms.py


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'company']  # Ensure fields match your Job model

from django import forms
from .models import Resume, QuestionnaireResponse

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['resume_file']

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = QuestionnaireResponse
        fields = ['question', 'answer']
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['full_name', 'email', 'resume', 'cover_letter']
