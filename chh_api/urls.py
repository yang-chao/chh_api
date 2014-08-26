from django.conf.urls import include, url
from django.contrib import admin
from chh import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'chh_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/(\d{1,2})/(\d{1,3})/$', views.news),

]
