from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', 'index'),
    #url(r'^admin/', include(admin.site.urls)),
    # ... your url patterns
]
# urlpatterns = ('pawn.views',
#     # Examples:
#     # url(r'^$', 'PawnShop.views.home', name='home'),
#     # url(r'^PawnShop/', include('PawnShop.foo.urls')),
#      url(r'^$', 'index'),
#      #url(r'^(?P<pledge_id>\d+)/$', 'pledge'),
#      #url(r'^(?P<pledge_id>\d+)/redemption/$', 'redemption'),
# )