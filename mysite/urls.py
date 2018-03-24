from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]