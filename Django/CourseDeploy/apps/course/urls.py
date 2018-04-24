from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
	url(r'^$', views.index),
	url(r'^courses$', views.mainindex),
	url(r'^comment/(?P<user_id>\d+)$', views.show),
	url(r'^courses/create$', views.process_new),
	url(r'^courses/destroy/(?P<user_id>\d+)$', views.delete),
	url(r'^destroy/(?P<user_id>\d+)$', views.delete2),
 # This line has changed!
]



# url(r'^users/new$', views.create),
# url(r'^users/create$', views.process_new),
# url(r'^users/(?P<user_id>\d+)/edit$', views.update),
# url(r'^update/(?P<user_id>\d+)$', views.update2),
# url(r'^users/(?P<user_id>\d+)/destroy$', views.delete),
# url(r'^destroy/(?P<user_id>\d+)$', views.delete2),
# url(r'^reset$', views.reset)