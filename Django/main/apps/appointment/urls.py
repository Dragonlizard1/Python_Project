from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),
url(r'^main$', views.mainindex),
url(r'^logout$', views.logout),
url(r'^register$', views.register),
url(r'^login$', views.login),
url(r'^appointments$', views.appointment),
url(r'^process$', views.process),
url(r'^update/(?P<appoint_id>\d+)$', views.update),
url(r'^update2/(?P<appoint_id>\d+)$', views.update2),
url(r'^delete/(?P<appoint_id>\d+)$', views.delete)
# This line has changed!
]