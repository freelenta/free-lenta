from django.conf.urls import patterns, include, url
from news_site import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'free_lenta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^(?P<pk>\d+)/detail/$',views.DetailView.as_view(), name='detail'),
    url(r'^(?P<cat_id>\w+)/category/$',views.category, name='category'),
    url(r'^about/$',views.about, name='about'),
    url(r'^help/$',views.help, name='help'),
)
