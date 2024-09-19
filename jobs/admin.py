from django.contrib import admin
from .models import Job, JobApplication, Resume, QuestionnaireResponse

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'posted_by', 'posted_date')
    search_fields = ('title', 'company', 'location')
    list_filter = ('posted_by', 'posted_date')

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'job', 'applied_on')
    search_fields = ('full_name', 'email', 'job__title')
    list_filter = ('job', 'applied_on')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'resume_file')
    search_fields = ('user__username',)

@admin.register(QuestionnaireResponse)
class QuestionnaireResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'question')
    search_fields = ('user__username', 'job__title', 'question')
