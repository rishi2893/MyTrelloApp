from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^boards/$', views.index_data, name='index_data'),
    url(r'^cards/(?P<board_id>[0-9]+)/$', views.board_data, name='board_data'),
    url(r'^lists/(?P<card_id>[0-9]+)/$', views.card_data, name='card_data'),
    url(r'^(?P<board_id>[0-9]+)/$', views.board_detail, name='board_detail'),
]