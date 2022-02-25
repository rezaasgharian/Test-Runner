from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpResponse

from api.models import TestRunRequest, TestFilePath
from api.serializers import TestRunRequestSerializer, TestRunRequestItemSerializer
from api.tasks import execute_test_run_request
from api.usecases import get_assets


class TestRunRequestAPIView(ListCreateAPIView):
    serializer_class = TestRunRequestSerializer
    queryset = TestRunRequest.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        instance = serializer.save()
        execute_test_run_request.delay(instance.id)


class TestRunRequestItemAPIView(RetrieveAPIView):
    serializer_class = TestRunRequestItemSerializer
    queryset = TestRunRequest.objects.all()
    lookup_field = 'pk'


class AssetsAPIView(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK, data=get_assets())


class UploadTestFileAPIView(APIView):
    def post(self,request):
        files = request.FILES.getlist('files')
        for file in files:
            testFile = TestFilePath.objects.create(filePath=file,path=f'uploads/tests/{file.name}')
        return HttpResponse('success')