from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),
url(r'^main$', views.mainindex),
url(r'^register$', views.register),
url(r'^login$', views.login),
url(r'^dashboard$', views.dashboard),
url(r'^additem/(?P<user_id>\d+)$', views.additem),
url(r'^additem2/(?P<user_id>\d+)$', views.additem2),
url(r'^delete/(?P<item_id>\d+)$', views.delete),
url(r'^logout$', views.logout),
url(r'^addtofriend/(?P<item_id>\d+)$', views.addtofriend),
url(r'^wish_items/(?P<item_id>\d+)$', views.show),


# url(r'^logout$', views.logout),
# url(r'^register$', views.register),
# url(r'^login$', views.login),
# url(r'^appointments$', views.appointment),
# url(r'^process$', views.process),
# url(r'^update/(?P<appoint_id>\d+)$', views.update),
# url(r'^update2/(?P<appoint_id>\d+)$', views.update2),
# url(r'^delete/(?P<appoint_id>\d+)$', views.delete)
# This line has changed!
]