from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^pawnshop/', include('pawn.urls')),
    # Examples:
    # url(r'^$', 'pawnshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
