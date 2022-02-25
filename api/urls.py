from django.urls import path

from .views import TestRunRequestAPIView, TestRunRequestItemAPIView, AssetsAPIView, UploadTestFileAPIView

urlpatterns = [
    path('assets', AssetsAPIView.as_view(), name='assets'),
    path('upload-file', UploadTestFileAPIView.as_view(),name='upload_test_file'),
    path('test-run', TestRunRequestAPIView.as_view(), name='test_run_req'),
    path('test-run/<pk>', TestRunRequestItemAPIView.as_view(), name='test_run_req_item'),
]
