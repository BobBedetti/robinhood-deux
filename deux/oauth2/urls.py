from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

from deux.oauth2 import views

app_name = "oauth2"

urlpatterns = [
    re_path(r'^token/$', views.MFATokenView.as_view(), name="token"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
