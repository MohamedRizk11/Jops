from rest_framework.decorators import api_view
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



class joblistapi(generics.ListAPIView):
    queryset=Job.objects.all()
    serializer_class=Jobserailzers


class jobdetailapi(generics.RetrieveAPIView):
    queryset=Job.objects.all()
    serializer_class=Jobserailzers    