"""ClientPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^$', views.signup, name='signup'),

    url(r'^user/login/$', views.login, name='login'),

    url(r'^user/logout/$', views.logout, name='logout'),



    url(r'^user/un_confirm/$', views.unconfirm, name='un_confirm'),

    url(r'^user/re_confirm/$', views.resend_token, name='re_confirm'),

    url(r'^user/account_activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.account_activate, name='account_activate'),

    url(r'^user/reset_activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.reset_activate, name='reset_activate'),



    url(r'^user/forget_password/$', views.forget_password, name='forget_password'),

    url(r'^user/(?P<uidb64>[0-9A-Za-z_\-]+)/reset_password/$', views.reset_password, name='reset_password'),



    url(r'^dashboard/$', views.dashboard, name='dashboard'),

    # url(r'^client/new/$', views.client_detail, name='new'),

    # url(r'^property/new/$', views.client_property, name='property'),

    # url(r'^retainer/new/$', views.property_retainer, name='retainer'),




]
