from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView
from django.db.models import Q , F
from .models import Job ,jobapply 
from django.shortcuts import get_object_or_404
from .forms import JobApplyForm,jobform


def mydebug(request):
    data=Job.objects.select_related().all()
    return render(request,'job/debug.html',{"data":data})

# Create your views here.
def job_list(request):
    all_jobs=Job.objects.all()
    job_count=all_jobs.count()
    page = request.GET.get('page', 1)

    paginator = Paginator(all_jobs, 50)
    try:
        all_jobs = paginator.page(page)
    except PageNotAnInteger:
        all_jobs = paginator.page(1)
    except EmptyPage:
        all_jobs = paginator.page(paginator.num_pages)
    return render(request,'job/job_list.html',{'jobs':all_jobs,'job_count':job_count})



def job_detail(request,slug):
    job=Job.objects.get(slug=slug)
    return render(request,'job/job_detail.html',{'job':job})


class jobapply(CreateView):
    model=jobapply
    success_url='/jobs/'
    #fields=['username','email','cv','linked_url','github_url','coverlater']
    form_class=JobApplyForm

    def form_valid(self, form):
        slug = self.kwargs.get('slug')
        job=get_object_or_404(Job,slug=slug)
        job_apply=form.save(commit=False)
        job_apply.job=job
        job_apply.save()
        return super().form_valid(form)
    

class AddJob(CreateView)    :
    model=Job
    success_url='/jobs/'
   # fields=[ 'title','loction','company','salary_start','salary_end','description','vecancy','job_nature','experience','category']
    form_class=jobform