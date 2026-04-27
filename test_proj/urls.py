from django.urls import include, re_path

urlpatterns = [
    re_path(r"^mfa/", include("deux.urls")),
    re_path(r"^mfa/authtoken/", include(("deux.authtoken.urls", "authtoken"))),
    re_path(r"^mfa/oauth2/", include(("deux.oauth2.urls", "oauth2"))),
]
