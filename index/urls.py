from django.conf.urls import url

from index.views import *

urlpatterns = [
    url(r'^$',index_views),
    url(r'^login/$',login_views),
    url(r'^register/$',register_views),
    url(r'^01_server/$',server01_views),
    url(r'^02_server/$',server02_views),
    url(r'^03_server/$',server03_views),
    url(r'^04_server/$',server04_views),
    url(r'^checkLogin/$',checkLogin_views),
    url(r'^exit/$',exit_views),
    url(r'^loadGoods/$',loadGoods_views),
    url(r'^cart_count/$',cart_count_views),
]