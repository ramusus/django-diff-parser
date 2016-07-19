from django.conf.urls import url
from django.contrib import admin
from diff_parser.views import IndexView, ParseView

urlpatterns = [
    url(r'^admin/',     admin.site.urls),
    url(r'^$',          IndexView.as_view(), name="index"),
    url(r'^parse/$',    ParseView.as_view(), name="parse"),
]
