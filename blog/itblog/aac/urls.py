from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'tolistallmine/$', views.ToListAllMine),
    url(r'toaddarticle/$',views.ToAddArticle),
    # url('addarticle/$', views.AddArticle),
]