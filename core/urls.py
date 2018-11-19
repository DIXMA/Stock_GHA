from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^admin/', include('app.urls')),
    url(r'^$', RedirectView.as_view(url='app_manager/')),
    url(r'^app_manager/', include('app.urls')),
]
