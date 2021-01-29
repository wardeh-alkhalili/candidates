from django.urls import path,re_path
from . import views
from django.conf.urls import url

candidate_list = views.CandidatesListCreate.as_view({
    'get': 'get_all',
})

candidate_details = views.CandidatesListCreate.as_view({
    'get': 'details',
})

candidate_download_cv = views.CandidatesListCreate.as_view({
    'get': 'download',
})

candidate_create = views.CandidatesListCreate.as_view({
    'post': 'create',
})


urlpatterns = [
    url(r'^api/candidates/$', candidate_list, name='candidate_list'),
    url(r'^api/candidates/(?P<id>\d+)/details/$', candidate_details, name='candidate_details'),
    url(r'^api/candidates/(?P<id>\d+)/download_cv/$', candidate_download_cv, name='candidate_download_cv'),
    url(r'^api/candidates/register/$', views.Register.as_view()),
    url(r'^api/get-token', views.UserLogin.as_view(), name='get-token'),
]