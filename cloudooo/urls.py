from django.conf.urls.defaults import patterns, url
from views import CloudoooView

urlpatterns = patterns('',
    url(r'^$', CloudoooView.as_view()),
)
