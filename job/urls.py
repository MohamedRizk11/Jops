
from django.urls import path
from .views import job_list,job_detail
from .api import job_list_api ,job_detail_api,joblistapi,jobdetailapi

urlpatterns = [
    path('', job_list),
    path('<slug:slug>', job_detail),

    path('api/list/<int:pk>',jobdetailapi.as_view()),

    path('api/list',joblistapi.as_view())
    



]