
from django.urls import path
from .views import job_list,job_detail,jobapply,AddJob
from .api import job_list_api ,job_detail_api,joblistapi,jobdetailapi

urlpatterns = [
    path('', job_list),
    path('add/', AddJob.as_view()),
    path('<slug:slug>', job_detail),
    path('<slug:slug>/apply', jobapply.as_view()),
    path('api/list/<int:pk>',jobdetailapi.as_view()),

    path('api/list',joblistapi.as_view())
    



]