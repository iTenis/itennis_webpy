from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views
urlpatterns=[
    url(r'login/(\d+)/$',TemplateView.as_view(template_name="apc/login.html")),
    url(r'get_vaildcode_img/', views.Get_VaildCode_Img),
    url(r'send_mail/', views.SendMail),
    url(r'login_t/', views.Login),
    url(r'forget_t/', views.Forget),
    url(r'register_t/', views.Register),
    url(r'checkuser/(.*)/$', views.CheckUser),
    url(r'logout_t/', views.Logout),
    # url(r'test/',views.test),
]