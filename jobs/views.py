from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from .models import Job, JobApplication
from .forms import JobForm, JobApplicationForm

# Homepage view
def homepage(request):
    return render(request, 'homepage.html')

# View to post a job (requires login)
@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            return redirect('jobs:job_list')
    else:
        form = JobForm()
    return render(request, 'jobs/post_job.html', {'form': form})

# Job listing view with pagination
def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 10)  # Display 10 jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'jobs/job_list.html', {'page_obj': page_obj})

# Job detail view
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

# Apply for a job view (requires login)
@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.user = request.user
            application.save()

            try:
                send_mail(
                    subject=f"Application for {job.title}",
                    message=f"Thank you for applying for {job.title}.",
                    from_email='your-email@example.com',
                    recipient_list=[request.user.email],
                    fail_silently=False,
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            except Exception as e:
                return HttpResponse(f"An error occurred while sending the email: {e}")

            return redirect('jobs:job_list')
    else:
        form = JobApplicationForm()

    return render(request, 'jobs/apply_for_job.html', {
        'form': form,
        'job': job
    })

# User signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('jobs:job_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# User profile view (requires login)
@login_required
def profile(request):
    return render(request, 'registration/profile.html')

# View to delete a job (requires login)
@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        job.delete()
        return redirect('jobs:job_list')
    return render(request, 'jobs/confirm_delete.html', {'job': job})

# View to see job applications (requires login)
@login_required
def job_applications(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    applications = JobApplication.objects.filter(job=job)
    return render(request, 'jobs/job_applications.html', {'job': job, 'applications': applications})

# View for user to see all job applications for their posted jobs (requires login)
@login_required
def user_job_applications(request):
    jobs = Job.objects.filter(posted_by=request.user)
    applications = {job.id: JobApplication.objects.filter(job=job) for job in jobs}

    return render(request, 'jobs/user_job_applications.html', {
        'jobs': jobs,
        'applications': applications
    })

# Send a test email (for debugging or testing purposes)
def send_test_email(request):
    try:
        send_mail(
            'Test Subject',
            'Test Message',
            'your-email@example.com',
            ['recipient@example.com'],
            fail_silently=False,
        )
        return HttpResponse("Email sent successfully!")
    except BadHeaderError:
        return HttpResponse("Invalid header found.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")
