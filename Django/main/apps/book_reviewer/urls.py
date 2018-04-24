from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),
url(r'^main$', views.mainindex),
url(r'^logout$', views.logout),
url(r'^register$', views.register),
url(r'^login$', views.login),
url(r'^books$', views.books),
url(r'^add$', views.add),
url(r'^add2$', views.add2),
url(r'^book_review/(?P<book_id>\d+)$', views.book_review),
url(r'^add_review/(?P<book_id>\d+)$', views.add_review),






# url(r'^process$', views.process),
# url(r'^update/(?P<appoint_id>\d+)$', views.update),
# url(r'^update2/(?P<appoint_id>\d+)$', views.update2),
# url(r'^delete/(?P<appoint_id>\d+)$', views.delete)

]