"""testproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.urls import include, re_path

urlpatterns = [
    re_path(r"^api-auth/",
        include("rest_framework.urls", namespace="rest_framework")),
    re_path(r"^mfa/", include("deux.urls")),
    re_path(r"^mfa/authtoken/",
        include("deux.authtoken.urls", namespace="authtoken"),
    ),
    re_path(r"^mfa/oauth2/",
        include("deux.oauth2.urls", namespace="oauth2"),
    ),
]
