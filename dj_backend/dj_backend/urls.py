from django.conf.urls import patterns, include, url

from django.contrib import admin
from dj_api import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dj_backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/hello/', views.hello),

    url(r'^api/shopdetail/', views.shopdetail),
    url(r'^api/addshop/', views.addshop),
    url(r'^api/delshop/', views.delshop),
    url(r'^api/updateshop/', views.updateshop),
)
