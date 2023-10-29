from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import generics
from .serailzers import Jobserailzers
from .models import Job


@api_view(['GET'])
def job_list_api(request):
    jobs=Job.objects.all()
    data=Jobserailzers(jobs,many=True).data
    return Response({'Jobs':data})


@api_view(['GET'])
def job_detail_api(request,id):
    job=Job.objects.get(id=id)
    data=Jobserailzers(job).data
    return Response({'Job':data})



class joblistapi(generics.ListCreateAPIView):
    queryset=Job.objects.all()
    serializer_class=Jobserailzers
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['title', 'vecancy','job_nature']
    search_fields = ['title', 'salary_start', 'description']
    ordering_fields = ['experience', 'create_at']


class jobdetailapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Job.objects.all()
    serializer_class=Jobserailzers    