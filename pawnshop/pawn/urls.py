from django.conf.urls import url, include

urlpatterns = ('pawn.views',
    # Examples:
    # url(r'^$', 'PawnShop.views.home', name='home'),
    # url(r'^PawnShop/', include('PawnShop.foo.urls')),
     url(r'^$', 'index'),
     #url(r'^(?P<pledge_id>\d+)/$', 'pledge'),
     #url(r'^(?P<pledge_id>\d+)/redemption/$', 'redemption'),
)