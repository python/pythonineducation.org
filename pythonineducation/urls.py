from django.conf.urls import url

from .views import page_view

urlpatterns = [
    url(r'^$', page_view),
    url(r'^(?P<language>[\w-]+)/(?P<slug>[\w-]+)/$', page_view),
]
